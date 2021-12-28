from django.urls import path

from fscohort.views import index
from .views import index, student_delete, student_detail, student_list, student_add, student_update

urlpatterns = [
    path('', index, name='index'),
    path("student/", student_list, name="student"),
    path("student/<int:id>/", student_detail, name="detail"),
    path("student/<int:id>/update/", student_update, name="update"),
    path("student/<int:id>/delete/", student_delete, name="delete"),
    path("add/", student_add, name="add"),
]
