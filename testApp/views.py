from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView

from .models import Institution, Batch, Student
from authentication.permissions import CustomPermission
from .serializer import InstitutionSerializer, BatchSerializer, StudentSerializer


class CreateInstitutionView(CreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class ListIntitutionView(ListAPIView):
    query_set = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class UpdateInstitutionView(UpdateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes =  [CustomPermission]
    required_permission = []


class DeleteInstitutionView(DestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes =  [CustomPermission]
    required_permission = []


class CreateBatchView(CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class ListBatchView(ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [CustomPermission]
    required_permission = []
    

class UpdateBatchView(UpdateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class DeleteBatchView(DestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class CreateStudentView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class ListStudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class UpdateStudentView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class DeleteStudentView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermission]
    required_permission = []


class StudentDetailsAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer