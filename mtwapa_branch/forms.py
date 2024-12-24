# forms.py
from django import forms
from .models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'user', 'first_name', 'last_name', 'gender', 'phone', 'emergency_contact_name',
            'emergency_contact_phone', 'address', 'identification_no', 'specialization',
            'department', 'years_of_experience', 'available_days', 'profile_picture'
        ]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'phone', 'gender', 'email', 'Identification_no',
            'date_of_birth', 'address', 'emergency_contact_name', 'emergency_contact_number',
            'blood_type', 'allergies', 'chronic_conditions', 'medical_history',
            'insurance_provider', 'profile_picture'
        ]


class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'emergency_contact_name',
            'emergency_contact_phone', 'gender', 'Identification_no', 'assigned_doctor',
            'assigned_area', 'start_date', 'end_date', 'profile_picture'
        ]



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name', 'description', 'head', 'phone', 'email', 'research_focus'
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'reason', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = [
            'patient', 'doctor', 'date', 'visit_reason',
            'diagnosis', 'symptoms', 'physical_examination',
            'vital_signs', 'tests_ordered', 'test_results',
            'prescription', 'procedures', 'follow_up_date',
            'additional_notes',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'follow_up_date': forms.DateInput(attrs={'type': 'date'}),
        }
