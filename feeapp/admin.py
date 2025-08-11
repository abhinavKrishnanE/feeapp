from django.contrib import admin

from .models import FeeStructure, FeeComponent, Discount, StudentBatchFeeDetails, InstallmentDetails, InstallmentType, Payment, Notification, FeeNotification


admin.site.register(FeeComponent)
admin.site.register(FeeStructure)
admin.site.register(Discount)
admin.site.register(StudentBatchFeeDetails)
admin.site.register([InstallmentDetails, InstallmentType, Payment, Notification, FeeNotification])