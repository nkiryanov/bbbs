from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

from users.mixins import DynamicLookupMixin
from users.models import Profile
from users.utils import AdminOnlyPermissionsMixin


class ProfileInline(AdminOnlyPermissionsMixin, admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"
    filter_horizontal = ("region",)
    fields = (
        "role",
        "city",
        "region",
    )

    def get_fields(self, request, obj=None):
        if obj.profile.is_moderator_reg:
            return super().get_fields(self, request)
        fields = (
            "role",
            "city",
        )
        return fields


class UserAdmin(AdminOnlyPermissionsMixin, DynamicLookupMixin, UserAdmin):
    inlines = (ProfileInline,)

    list_display = (
        "id",
        "username",
        "is_active",
        "is_staff",
        "profile__role",
        "profile__city",
    )
    list_filter = (
        "is_active",
        "profile__role",
        "profile__city",
    )
    profile__role_short_description = "роль"
    profile__city_short_description = "город"
    list_display_links = ("username",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if request.user.profile.is_moderator_gen:
            fieldsets = (
                (None, {"fields": ("username", "email")}),
                (_("Personal info"), {"fields": ("first_name", "last_name")}),
                (
                    _("Permissions"),
                    {
                        "fields": (
                            "is_active",
                            "is_staff",
                            "is_superuser",
                        )
                    },
                ),
            )
            return fieldsets
        return super().get_fieldsets(request, obj)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = (
            qs
            .select_related("profile")
            .select_related("profile__city")
        )
        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            return form
        if not request.user.is_superuser:
            form.base_fields["is_superuser"].disabled = True
            form.base_fields["is_staff"].disabled = True
        return form

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

    def user_role(self, obj):
        return obj.profile.role

    def user_city(self, obj):
        return obj.profile.city

    def save_model(self, request, obj, form, change):
        """Should be deleted. All the logic in models."""
        if change:
            if obj.profile.is_mentor and not obj.is_superuser:
                obj.is_staff = False
            else:
                obj.is_staff = True
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        if not request.user.is_anonymous:
            return (
                request.user.profile.is_admin
                or request.user.profile.is_moderator_gen
            )
        return False


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
