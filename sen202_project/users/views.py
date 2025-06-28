# users/views.py
from rest_framework import viewsets
from .models import Address, Resume, Company_profile, CustomUser
from .serializers import AddressSerializer, ResumeSerializer, Company_profileSerializer, CustomUserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = Company_profile.objects.all()
    serializer_class = Company_profileSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
