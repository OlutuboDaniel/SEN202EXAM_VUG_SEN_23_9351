# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, ResumeViewSet, CompanyProfileViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'companies', CompanyProfileViewSet)
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
