from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import CustomUser, Permission, UserRole
from .serializer import CreateUserSerializer, CreateUserRoleSerializer, CreatePermissionSerializer, ListPermissionSerializer, ListUserRoleSerializer
from .permissions import CustomPermission


class CreateUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


class CreateUserRoleView(CreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = CreateUserRoleSerializer


class CreatePermissionView(CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = CreatePermissionSerializer


