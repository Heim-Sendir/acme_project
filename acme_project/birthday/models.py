from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age

User = get_user_model()


class Birthday(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        validators=(real_age,)
        )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        default='birthdays_images/not_logo.jpg'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор записи',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint'
            ),
        )

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('created_at',)
