from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.registration import RegistrationSerializer


class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject='Ваш код подтверждения YaMDb',
            message=f'Код подтверждения:{confirmation_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(user.email,)
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
