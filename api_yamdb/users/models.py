import uuid

import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал
    для создания User (для демонстрации).
    """

    def create_user(self, username, email, password=None, role='', bio=''):

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            role=role, bio=bio
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )

    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Пользовательские роли',
        blank=True,
        max_length=max(len(role[0]) for role in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default='user'
    )
    username = models.CharField(db_index=True,
                                max_length=255,
                                unique=True)
    email = models.EmailField(db_index=True, unique=True)
    last_login = models.DateTimeField(auto_now=True)

    confirmation_code = models.CharField(max_length=36,
                                         default=uuid.uuid4)
    objects = UserManager()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором
        хранится идентификатор этого
        пользователя, срок действия токена
        составляет 1 день от создания
        """
        dt = timezone.now() + timezone(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @property
    def token(self):
        return self._generate_jwt_token()

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER

    def __str__(self):
        return self.email
