from rest_framework.serializers import ModelSerializer
from .models import CustomUser, UserRole, Permission


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'contact_no', 'user_role', 'user_permission']

    def create(self, validated_data):
        user_permission = validated_data.pop('user_permission', [])
        user = CustomUser.objects.create_user(**validated_data)
        user.user_permission.set(user_permission)
        return user
    

class CreateUserRoleSerializer(ModelSerializer):
    class Meta:
        model = UserRole
        fields = ["user_role", "permissions"]


class CreatePermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ["name"]


class ListPermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ["name"]


class ListUserRoleSerializer(ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['user_role']