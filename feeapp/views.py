from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from datetime import timedelta, date
import requests

from .models import FeeStructure, FeeComponent, Discount, InstallmentDetails, Payment, Notification, FeeNotification
from .serializer import FeestructureSerializer, FeeComponentSerializer, InstallmentTypeSerializer, StudentBatchFeeDetails
from .serializer import  DiscountSerializer, InstallmentDetailsSerializer, PaymentSerializer, NotificationSerializer, FeeNotificationSerializer
from .serializer import StudentBatchFeeDetailsSerializer
from authentication.permissions import CustomPermission


class FeeStructureListView(ListAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeestructureSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeStructureCreateView(CreateAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeestructureSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeStructureUpdateView(UpdateAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeestructureSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeStructureDeleteView(DestroyAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeestructureSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeComponentListView(ListAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = FeeComponentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeComponentCreateView(CreateAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = FeeComponentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeComponentUpdateView(UpdateAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = FeeComponentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeComponentDeleteView(DestroyAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = FeeComponentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentTypeListView(ListAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = InstallmentTypeSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentTypeCreateView(CreateAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = InstallmentTypeSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentTypeUpdateView(UpdateAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = InstallmentTypeSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentTypeDeleteView(DestroyAPIView):
    queryset = FeeComponent.objects.all()
    serializer_class = InstallmentTypeSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class DiscountCreateView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class DiscountUpdateView(UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class DiscountDeleteView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentDetailsListView(ListAPIView):
    queryset = InstallmentDetails.objects.all()
    serializer_class = InstallmentDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentDetialsCreateView(CreateAPIView):
    queryset = InstallmentDetails.objects.all()
    serializer_class = InstallmentDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentDetailsUpdateView(UpdateAPIView):
    queryset = InstallmentDetails.objects.all()
    serializer_class = InstallmentDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class InstallmentDetailsDeleteView(DestroyAPIView):
    queryset = InstallmentDetails.objects.all()
    serializer_class = InstallmentDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class PaymentUpdateView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class PaymentDeleteView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class NotificationCreateView(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class NotificationUpdateView(UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class NotificationDeleteView(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeNotificationListView(ListAPIView):
    queryset = FeeNotification.objects.all()
    serializer_class = FeeNotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeNotificationCreateView(CreateAPIView):
    queryset = FeeNotification.objects.all()
    serializer_class = FeeNotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeNotificationUpdateView(UpdateAPIView):
    queryset = FeeNotification.objects.all()
    serializer_class = FeeNotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class FeeNotificationDeleteView(DestroyAPIView):
    queryset = FeeNotification.objects.all()
    serializer_class = FeeNotificationSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class StudentFeeBatchDetialsListView(ListAPIView):
    queryset = StudentBatchFeeDetails.objects.all()
    serializer_class = StudentBatchFeeDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class StudentBatchFeeDetailsCreateView(CreateAPIView):
    queryset = StudentBatchFeeDetails.objects.all()
    serializer_class = StudentBatchFeeDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class StudentBatchFeeDetailsUpdateView(UpdateAPIView):
    queryset = StudentBatchFeeDetails.objects.all()
    serializer_class = StudentBatchFeeDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class StudentBatchFeeDetialsDeleteView(DestroyAPIView):
    queryset = StudentBatchFeeDetails.objects.all()
    serializer_class = StudentBatchFeeDetailsSerializer
    permission_classes = [CustomPermission]
    required_permission = []


