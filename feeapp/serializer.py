from rest_framework.serializers import ModelSerializer, SerializerMethodField

import requests

from .models import FeeStructure, FeeComponent, InstallmentType, Discount, InstallmentDetails, Payment, Notification, FeeNotification, StudentBatchFeeDetails
from authentication.serializer import *


class FeestructureSerializer(ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = '__all__'


class FeeComponentSerializer(ModelSerializer):
    class Meta:
        model = FeeComponent
        fields = '__all__'

    
class InstallmentTypeSerializer(ModelSerializer):
    class Meta:
        model = InstallmentType
        fields = '__all__'

    
class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class InstallmentDetailsSerializer(ModelSerializer):
    class Meta:
        model = InstallmentDetails
        fields = '__all__'

    
class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    
class FeeNotificationSerializer(ModelSerializer):
    class Meta:
        model = FeeNotification
        fields = "__all__"


class StudentBatchFeeDetailsSerializer(ModelSerializer):
    class Meta:
        model = StudentBatchFeeDetails
        fields = '__all__'