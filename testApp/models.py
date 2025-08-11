from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model



User = get_user_model()


class Institution(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_no = models.CharField(max_length=12)
    email = models.EmailField()
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)


class Batch(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration_in_months = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact_no = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class StudentBatch(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student} {self.batch}"