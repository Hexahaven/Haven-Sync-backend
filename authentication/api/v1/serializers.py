from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
import re

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    full_name = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'password')

    def validate_full_name(self, value):
        if not value or value.isspace():
            raise serializers.ValidationError("Full name cannot be empty.")
        if not re.match("^[a-zA-Z ]+$", value):
            raise serializers.ValidationError("Full name can only contain letters and spaces.")
        if len(value) < 3 or len(value) > 50:
            raise serializers.ValidationError("Full name must be between 3 and 50 characters.")
        return value.strip()
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user

class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
