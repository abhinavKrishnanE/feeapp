from django.db import models


class StudentBatchFeeDetails(models.Model):
    student_id = models.IntegerField()
    batch_id = models.IntegerField()
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)
    selected_installment = models.ForeignKey('InstallmentType', on_delete= models.CASCADE)
    fee_structure = models.ForeignKey('FeeStructure', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.student_id} {self.batch_id}"
    
    
class FeeStructure(models.Model):
    name = models.CharField(max_length=20)

    due_types = [('fixed','Fixed'), ('joining_date', 'Joining_Date')]
    due_type = models.CharField(max_length=50, choices=due_types)

    fixed_due_date = models.PositiveIntegerField(null=True, blank=True)
    batch = models.IntegerField()

    def __str__(self):
        return self.name


class FeeComponent(models.Model):
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_upfront = models.BooleanField(default=False)


class InstallmentType(models.Model):
    installment_choices = [('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('custom', 'Custom')]
    insatllment_choice = models.CharField(max_length=30, choices=installment_choices)

    days = models.PositiveIntegerField(null=True, blank=True)


class Discount(models.Model):
    name = models.CharField(max_length=100)
    
    discount_types = [('percentage', 'Percentage'), ('amount', 'Amount')]
    discount_type = models.CharField(max_length=30, choices=discount_types)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class InstallmentDetails(models.Model):
    installment_type = models.ForeignKey(InstallmentType, on_delete=models.CASCADE)
    installment_number = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=4, decimal_places=2)


class Payment(models.Model):
    student_id = models.IntegerField()
    installment_details = models.ForeignKey(InstallmentDetails, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)


class Notification(models.Model):
    student_id = models.IntegerField()
    title = models.CharField(max_length=100)
    message = models.TextField()


class FeeNotification(models.Model):
    student_batch_fee_details = models.OneToOneField(StudentBatchFeeDetails, on_delete=models.CASCADE)
    notify_before_days = models.IntegerField()