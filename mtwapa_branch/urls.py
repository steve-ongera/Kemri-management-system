# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    path('interns/', views.intern_list, name='intern_list'),
    path('interns/<int:pk>/', views.intern_detail, name='intern_detail'),
    path('interns/add/', views.intern_create, name='intern_create'),
    path('interns/<int:pk>/edit/', views.intern_update, name='intern_update'),
    path('interns/<int:pk>/delete/', views.intern_delete, name='intern_delete'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('departments/add/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    path('medical-records/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    path('medical-records/add/', views.medical_record_create, name='medical_record_create'),
    path('medical-records/<int:pk>/edit/', views.medical_record_update, name='medical_record_update'),
    path('medical-records/<int:pk>/delete/', views.medical_record_delete, name='medical_record_delete'),
]

