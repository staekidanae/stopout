from django.shortcuts import render
from django.http import HttpResponse
from .models import School, Student

def index(request):
    return HttpResponse("STOPOUT")

def school_list():
    list_school = School.objects.order_by('name')
    return HttpResponse(list_school)

def school_detail():
    pass

def student_list():
    list_student = Student.objects.order_by('name')
    return HttpResponse(list_student)

def student_detail():
    pass
