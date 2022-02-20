from rest_framework import serializers
from reviews.models import Title

from .category import CategorySerializer
from .genre import GenreSerializer


class TitleInputSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'genre',
                  'category', 'description', 'rating')
