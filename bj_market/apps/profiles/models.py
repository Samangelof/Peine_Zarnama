from django.db import models
from auths.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.email
    

class BusinessProfile(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_business_account = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True)
    registration_documents = models.FileField(upload_to='registration_documents', blank=True, null=True)

    def __str__(self):
        return self.user.email
