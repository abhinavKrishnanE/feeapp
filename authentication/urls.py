from django.urls import path
from .views import CreateUserView, CreateUserRoleView, CreatePermissionView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("userrole/", CreateUserRoleView.as_view()),
    path("permission/", CreatePermissionView.as_view()),
    path("createuser/", CreateUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]