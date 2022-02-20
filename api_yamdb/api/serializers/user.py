from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        message = 'Эта почта используется другим пользователем'
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(message)
        return email

    def validate_username(self, username):
        message = 'Эта почта используется другим пользователем'
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(message)
        return username

    class Meta:
        model = User
        fields = ('email', 'username',
                  'bio', 'role',
                  'first_name', 'last_name',)
