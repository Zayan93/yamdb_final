from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User

from ..serializers.token import TokenSerializer


class CustomJWTTokenView(generics.CreateAPIView):
    serializer_class = TokenSerializer

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            username=serializer.validated_data.get('username')
        )
        token = AccessToken.for_user(user)
        confirmation_code = user.confirmation_code
        in_confirmation_code = serializer.validated_data.get(
            'confirmation_code'
        )
        if confirmation_code == in_confirmation_code:
            return Response({'Token': str(token)}, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
