from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from fscohort.forms import StudentForm

from fscohort.models import Student

# Create your views here.


def index(request):
    context = {
        'title': 'Welcome'
    }
    return render(request, 'fscohort/index.html', context)


def student_list(request):
    students = Student.objects.all()

    context = {
        'student': students
    }

    return render(request, 'fscohort/student-list.html', context)


def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'fscohort/student-add.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)

    context = {
        'student': student
    }

    return render(request, 'fscohort/student-detail.html', context)


def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')

    context = {
        'student': student,
        'form': form
    }

    return render(request, 'fscohort/student-update.html', context)


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student')

    context = {
        'student': student
    }
    return render(request, 'fscohort/student-delete.html', context)
