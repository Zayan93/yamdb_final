from rest_framework import serializers
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Выбериту другой username')
        return value
