# users/serializers.py

from rest_framework import serializers
from .models import Address, Resume, Company_profile, CustomUser  # Import your models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  # or list fields like ['id', 'username', 'email', 'dob']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class Company_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_profile
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
