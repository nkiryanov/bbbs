from django.db import models
<<<<<<< HEAD
from common.models import City
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
=======
from django.conf import settings
from common.models import City
>>>>>>> events


class Profile(models.Model):
    class Role(models.TextChoices):
        MENTOR = "mentor"
        MODERATOR_REG = "moderator_regional"
        MODERATOR_GEN = "moderator_general"
        ADMIN = "admin"

<<<<<<< HEAD
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    city = models.ForeignKey(City, on_delete=models.SET_NULL,
                             null=True)
=======
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    city = models.OneToOneField(
        City, related_name="profile", on_delete=models.RESTRICT
    )
>>>>>>> events
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.MENTOR
    )

    def __str__(self):
<<<<<<< HEAD
        return 'Профиль пользователя'

    @receiver(post_save, sender=User)
    def create_and_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
=======
        return "Профиль пользователя {}".format(self.user.username)
>>>>>>> events

    @property
    def is_admin(self):
        return self.Role.ADMIN == self.role

    @property
    def is_moderator_reg(self):
        return self.Role.MODERATOR_REG == self.role

    @property
    def is_moderator_gen(self):
        return self.Role.MODERATOR_GEN == self.role

    @property
    def is_mentor(self):
        return self.Role.MENTOR == self.role
