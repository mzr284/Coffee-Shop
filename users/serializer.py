from rest_framework import serializers
from .models import User, UserPofile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "data_joined", "phone_number", "is_staff"]



