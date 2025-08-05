from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import CreatePermissionView, CreateUserRoleView, CreateUserView
from .views import FeeStructureListView, FeeStructureCreateView, FeeStructureUpdateView, FeeStructureDeleteView
from .views import FeeComponentCreateView, FeeComponentListView, FeeComponentUpdateView, FeeComponentDeleteView
from .views import InstallmentTypeCreateView, InstallmentTypeListView, InstallmentTypeUpdateView, InstallmentTypeDeleteView
from .views import DiscountCreateView, DiscountListView, DiscountUpdateView, DiscountDeleteView
from .views import InstallmentDetailsListView, InstallmentDetialsCreateView, InstallmentDetailsUpdateView, InstallmentDetailsDeleteView
from .views import PaymentCreateView, PaymentListView, PaymentDeleteView, PaymentUpdateView
from .views import NotificationCreateView, NotificationDeleteView, NotificationListView, NotificationUpdateView
from .views import FeeNotificationCreateView, FeeNotificationDeleteView, FeeNotificationListView, FeeNotificationUpdateView
from .views import StudentFeeBatchDetialsListView, StudentBatchFeeDetialsDeleteView, StudentBatchFeeDetailsCreateView, StudentBatchFeeDetailsUpdateView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("permission/", CreatePermissionView.as_view()),
    path("userrole/", CreateUserRoleView.as_view()),
    path("createuser/", CreateUserView.as_view()),

    path("feestructure/", FeeStructureListView.as_view()),
    path("feestructure/create/", FeeStructureCreateView.as_view()),
    path("feestructure/update/<int:pk>/", FeeStructureUpdateView.as_view()),
    path("feestructure/delete/<int:pk>/", FeeStructureDeleteView.as_view()),

    path("feecomponent/", FeeComponentListView.as_view()),
    path("feecomponent/create/", FeeComponentCreateView.as_view()),
    path("feecomponent/update/<int:pk>/", FeeComponentUpdateView.as_view()),
    path("feecomponent/delete/<int:pk>/", FeeComponentDeleteView.as_view()),

    path("installmenttype/", InstallmentTypeListView.as_view()),
    path("installmenttype/create/", InstallmentTypeCreateView.as_view()),
    path("installmenttype/update/<int:pk>/", InstallmentTypeUpdateView.as_view()),
    path("installmenttype/delete/<int:pk>/", InstallmentTypeDeleteView.as_view()),

    path("discount/", DiscountListView.as_view()),
    path("discount/create/", DiscountCreateView.as_view()),
    path("discount/update/<int:pk>/", DiscountUpdateView.as_view()),
    path("discount/delete/<int:pk>/", DiscountDeleteView.as_view()),
    
    path("installmentdetails/", InstallmentDetailsListView.as_view()),
    path("installmentdetails/create/", InstallmentDetialsCreateView.as_view()),
    path("installmentdetiais/update/<int:pk>/", InstallmentDetailsUpdateView.as_view()),
    path("installmentdetails/delete/<int:pk>/", InstallmentDetailsDeleteView.as_view()),

    path("payment/", PaymentListView.as_view()),
    path("payment/create/", PaymentCreateView.as_view()),
    path("payment/update/<int:pk>/", PaymentUpdateView.as_view()),
    path("payment/delete/<int:pk>/", PaymentDeleteView.as_view()),

    path("notification/", NotificationListView.as_view()),
    path("notification/create/", NotificationCreateView.as_view()),
    path("notification/update/<int:pk>/", NotificationUpdateView.as_view()),
    path("notification/delete/<int:pk>/", NotificationDeleteView.as_view()),

    path("feenotification/", FeeNotificationListView.as_view()),
    path("feenotification/create/", FeeNotificationCreateView.as_view()),
    path("feenotification/update/<int:pk>/", FeeNotificationUpdateView.as_view()),
    path("feenotification/delete/<int:pk>/", FeeNotificationDeleteView.as_view()),

    path("studentbatchfeedetails/", StudentFeeBatchDetialsListView.as_view()),
    path("studentbatchfeedetails/create/", StudentBatchFeeDetailsCreateView.as_view()),
    path("studentbatchfeedetails/update/<int:pk>/", StudentBatchFeeDetailsUpdateView.as_view()),
    path("studentbatchfeedetails/delete/<int:pk>/", StudentBatchFeeDetialsDeleteView.as_view()),
]