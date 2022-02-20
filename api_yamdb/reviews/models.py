from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

from .validators import year_validator


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='category_name')
    slug = models.SlugField(unique=True, verbose_name='category_slug')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='category_name')
    slug = models.SlugField(unique=True, verbose_name='category_slug')

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='title_name')
    year = models.PositiveSmallIntegerField(
        validators=[year_validator],
        verbose_name="Year"
    )
    description = models.CharField(max_length=200, verbose_name='description')
    genre = models.ManyToManyField(
        Genre,
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles'
    )

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField(verbose_name='text')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='review',
    )
    score = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
        verbose_name='score'
    )
    pub_date = models.DateField('date published',
                                auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'отзыв'
        verbose_name_plural = 'review'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )
        ]

    def __str__(self):
        return self.title.name


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='authors_comments'
    )
    pub_date = models.DateField('date published',
                                auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text
