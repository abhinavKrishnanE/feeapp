from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        required_permission = getattr(view, 'required_permission', None)
        
        if isinstance(required_permission, str):
            required_permission = [required_permission]

        if not required_permission:
            return True
        
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True
        
        count = 0
        # role_permission = user.user_role.permissions.filter(name__in=required_permission)
        for permission in required_permission:
            role_permission = user.user_role.permissions.filter(name=permission)
            user_permission = user.user_permission.filter(name=permission)

            if role_permission or user_permission:
                count = count + 1

        if count == len(required_permission):
            return True

        return False
    