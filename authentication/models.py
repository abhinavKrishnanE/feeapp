from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Permission(models.Model):
    name = models.CharField(max_length=30, blank=True)

    
    def __str__(self):
        return self.name

    
class UserRole(models.Model):
    user_role = models.CharField(max_length=30, blank=True)
    permissions = models.ManyToManyField(Permission, null = True, blank=True)

    def __str__(self):
        return self.user_role


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact_no = models.CharField(max_length=12)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True)
    user_permission = models.ManyToManyField(Permission, null=True, blank=True)
