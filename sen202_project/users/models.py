from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Address(models.Model):
    house_number = models.CharField(max_length=10)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def str(self):
        return f"{self.house_number}, {self.street}, {self.city}, {self.state} {self.postal_code}"
    
class Resume(models.Model):
    education_level = models.CharField(max_length=100)
    completed_projects = models.CharField(max_length=255)
    previous_jobs = models.CharField(max_length=255) 
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def str(self):
        return f"{self.education_level}, {self.completed_projects}, {self.previous_jobs}, {self.custom_User} {self.address}"

class Company_profile(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    company_email = models.EmailField(unique=True)
    company_phone_number = models.CharField(max_length=20)
    company_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def str(self):
            return f"{self.company_name}, {self.industry}, {self.address}"

  
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    company_profile = models.ForeignKey(Company_profile, on_delete=models.CASCADE, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

    def str(self):
        return f"{self.first_name} {self.last_name}"