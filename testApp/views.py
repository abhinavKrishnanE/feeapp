from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Institution, Batch, Student, StudentBatch
from authentication.permissions import CustomPermission
from .serializer import InstitutionSerializer, BatchSerializer, StudentSerializer, StudentBatchSerializer


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


class StudentDetailsAPI(APIView):
    def post(self, request, *args, **kwargs):
        student_ids = request.data.get('student_ids', [])

        students = Student.objects.filter(id__in=student_ids)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class StudentBatchDetailsAPI(APIView):
    def post(self, request, *args, **kwargs):
        studet_batch_details  = StudentBatch.objects.all()
        serializer = StudentBatchSerializer(studet_batch_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)