from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schools/', views.school_list(), name='school_list'),
    path('schools/<int:school.id>/', views.school_detail(), name='school_detail'),
    path('student/', views.student_list(), name='student_list'),
    path('student/<int:school.id>/', views.student_detail(), name='student_detail'),
]
