from django.urls import path

from .views import CreateInstitutionView, ListIntitutionView, UpdateInstitutionView, DeleteInstitutionView
from .views import CreateBatchView, ListBatchView, UpdateBatchView, DeleteBatchView
from .views import ListStudentView, CreateStudentView, UpdateStudentView, DeleteStudentView
from .views import StudentDetailsAPI, StudentBatchDetailsAPI


urlpatterns = [
    path("institution/", ListIntitutionView.as_view()),
    path("institution/create/", CreateInstitutionView.as_view()),
    path("institution/update/<int:pk>/", UpdateInstitutionView.as_view()),
    path("institution/delete/<int:pk>/", DeleteInstitutionView.as_view()),

    path("batch/", ListBatchView.as_view()),
    path("batch/create/", CreateBatchView.as_view()),
    path("batch/update/<int:pk>/", UpdateBatchView.as_view()),
    path("batch/delete/<int:pk>/", DeleteBatchView.as_view()),

    path("student/", ListStudentView.as_view()),
    path("student/create/", CreateStudentView.as_view()),
    path("student/update/<int:pk>/", UpdateStudentView.as_view()),
    path("student/delete/<int:pk>/", DeleteStudentView.as_view()),

    path("studentdetailsapi/", StudentDetailsAPI.as_view()),
    path("studentbatchdetailsapi/", StudentBatchDetailsAPI.as_view()),
]