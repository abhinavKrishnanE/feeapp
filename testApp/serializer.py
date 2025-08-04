from rest_framework.serializers import ModelSerializer

from .models import Institution, Batch, Student, StudentBatch
from authentication.serializer import *


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class BatchSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

    
class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    
class StudentBatchSerializer(ModelSerializer):
    class Meta:
        model = StudentBatch
        fields = "__all__"

