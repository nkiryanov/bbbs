from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models

from common.utils.slugify import slugify


class Guide(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название статьи",
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание статьи",
    )
    image_caption = models.CharField(
        max_length=200,
        verbose_name="Описание к фотографии",
    )
    image_url = models.ImageField(
        blank=True,
        verbose_name="Фото статьи",
        help_text="Добавить фото",
        upload_to="entertainment/guides/",
    )
    text = models.TextField(
        verbose_name="Текст статьи",
    )

    class Meta:
        verbose_name = "Статья справочника"
        verbose_name_plural = "Статьи справочника"
        ordering = ["id"]

    def __str__(self):
        return self.title


class MovieTag(models.Model):
    name = models.CharField(
        verbose_name="Название тега", max_length=50, unique=True, null=True
    )
    slug = models.SlugField(
        verbose_name="Адрес тега", max_length=50, unique=True, null=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег (Фильмы)"
        verbose_name_plural = "Теги (Фильмы)"

    def __str__(self):
        return self.name


class Movie(models.Model):
    tags = models.ManyToManyField(
        MovieTag,
        related_name="movies",
        verbose_name="Теги",
        blank=False,
    )
    link = models.URLField(
        verbose_name="Ссылка на фильм",
        null=True,
        blank=False,
        max_length=250,
    )
    title = models.CharField(
        null=True,
        blank=False,
        max_length=100,
        unique=True,
        verbose_name="Название фильма",
    )
    producer = models.CharField(verbose_name="Режиссер", max_length=255)
    year = models.PositiveSmallIntegerField(verbose_name="Год")
    description = models.TextField(verbose_name="Описание фильма")
    image_url = models.URLField(
        verbose_name="Ссылка на превью",
        null=True,
        blank=False,
        max_length=250,
    )
    duration = models.DurationField(
        null=True, blank=True, verbose_name="Продолжительность фильма"
    )

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["id"]

    def __str__(self):
        return self.title

    def clean(self):
        if "youtube.com" not in self.link:
            raise ValidationError("Ссылка должна быть с youtube.com")

    def save(self, *args, **kwargs):
        watch_id = self.link.split("watch?v=")
        if "https://www.youtube.com/" in watch_id:
            embed_link = f"https://www.youtube.com/embed/{watch_id[1]}"
            self.link = embed_link
            self.image_url = (
                f"https://i.ytimg.com/vi/{watch_id[1]}/maxresdefault.jpg"
            )
        else:
            if self.link not in Movie.objects.all():
                watch_id = self.link.split("embed/")
                self.image_url = (
                    f"https://i.ytimg.com/vi/{watch_id[1]}/maxresdefault.jpg"
                )
        super().save(*args, **kwargs)


class VideoTag(models.Model):
    name = models.CharField(
        verbose_name="Название тега", max_length=50, unique=True
    )
    slug = models.SlugField(
        verbose_name="Адрес тега", max_length=50, unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег (Видео)"
        verbose_name_plural = "Теги (Видео)"

    def __str__(self):
        return self.name


class Video(models.Model):
    tags = models.ManyToManyField(
        VideoTag,
        blank=False,
        related_name="videos",
    )
    link = models.URLField(
        max_length=250,
        unique=True,
        verbose_name="Ссылка на видео",
    )
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название видео",
    )
    author = models.CharField(max_length=200, verbose_name="Автор")
    pub_date = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
    )
    preview = models.ImageField(
        blank=True,
        verbose_name="Картинка к видео",
        upload_to="entertainment/videos/",
    )
    duration = models.DurationField(
        null=True, verbose_name="Продолжительность видео"
    )

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ["id"]

    def __str__(self):
        return self.title


class BookTag(models.Model):
    name = models.CharField(
        verbose_name="Название тега", max_length=50, unique=True
    )
    slug = models.SlugField(
        verbose_name="Адрес тега", max_length=50, unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег (Книга)"
        verbose_name_plural = "Теги (Книги)"

    def __str__(self):
        return self.name


class Book(models.Model):
    tags = models.ManyToManyField(
        BookTag,
        blank=False,
        related_name="books",
    )
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название книги",
    )
    author = models.CharField(max_length=200, verbose_name="Автор")
    year = models.PositiveSmallIntegerField(verbose_name="Год")
    description = models.TextField(verbose_name="Описание")
    color = ColorField(
        max_length=30,
        verbose_name="Цвет обложки на странице",
    )
    link = models.URLField(
        max_length=250,
        blank=False,
        unique=True,
        verbose_name="Ссылка на книгу",
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Article(models.Model):
    is_main = models.BooleanField(
        verbose_name="Основная статья",
        default=False,
    )
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название статьи",
    )
    author = models.CharField(max_length=200, verbose_name="Автор")
    profession = models.CharField(max_length=200, verbose_name="Профессия")
    text = models.TextField(verbose_name="Текст")
    color = ColorField(
        max_length=30,
        verbose_name="Цвет обложки на странице",
    )
    image_url = models.ImageField(
        blank=True,
        verbose_name="Обложка",
        help_text="Добавить фото",
        upload_to="entertainment/articles/",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["id"]

    def __str__(self):
        return self.title

    def clean(self):
        is_main = Article.objects.filter(is_main=True).first()
        if is_main != self and self.is_main and is_main:
            raise ValidationError(
                "Чтобы выбрать данную статью, "
                "необходимо деактивировать "
                f"статью №{is_main.pk}"
            )

    def save(self, *args, **kwargs):
        is_main = Article.objects.filter(is_main=True)
        if is_main.exists() and is_main.first() != self:
            self.is_main = False
        super().save(*args, **kwargs)
