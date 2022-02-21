from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, write_only=True)
    confirmation_code = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']
    
    @classmethod
    def get_token(cls, user):
        token = AccessToken.for_user(user)
        return token
