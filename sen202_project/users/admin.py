from django.contrib import admin
from .models import CustomUser, Company_profile, Address, Resume


admin.site.register(CustomUser)
admin.site.register(Company_profile)
admin.site.register(Address)
admin.site.register(Resume)
