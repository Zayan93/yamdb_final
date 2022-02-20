from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Comment, Review

from ..permissions import ModeratorOrReadOnly
from ..serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (ModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def _get_review(self):
        return get_object_or_404(Review,
                                 pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self._get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self._get_review())
