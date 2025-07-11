from rest_framework import serializers
from users.models import User
from djoser.serializers import UserSerializer as DjoserUserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address']


class CustomDjoserUserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        ref_name = 'DjoserUserSerializer'

        