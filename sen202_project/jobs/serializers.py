#jobs/serializers.py
from rest_framework import serializers
from .models import Job, Application 

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'  # or list fields like ['id', 'username', 'email', 'dob']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
