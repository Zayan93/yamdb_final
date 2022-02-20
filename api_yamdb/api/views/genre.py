from rest_framework import viewsets
from reviews.models import Genre

from ..serializers.genre import GenreSerializer
from .category import ViewsMixin


class GenreViewSet(ViewsMixin, viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
