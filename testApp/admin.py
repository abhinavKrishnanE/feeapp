from django.contrib import admin

from .models import Student, Institution, Batch, StudentBatch
# Register your models here.

admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(StudentBatch)
admin.site.register(Institution)


