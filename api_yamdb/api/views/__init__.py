from .category import CategoryViewSet
from .comment import CommentViewSet
from .customjwttoken import CustomJWTTokenView
from .genre import GenreViewSet
from .registation import RegistrationView
from .review import ReviewViewSet
from .title import TitleViewSet
from .user import UserViewSet

__all__ = [
    "GenreViewSet",
    "TitleViewSet",
    "ReviewViewSet",
    "CommentViewSet",
    "RegistrationView",
    "CustomJWTTokenView",
    "CategoryViewSet",
    "UserViewSet",
]
