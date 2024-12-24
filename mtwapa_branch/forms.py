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


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'identification_no',
            'date_of_birth', 'gender', 'profile_picture', 'position',
            'department', 'employee_id', 'date_hired', 'contract_type',
            'salary', 'shift', 'address', 'city', 'region', 'emergency_contact_name',
            'emergency_contact_phone', 'access_level', 'is_active',
            'qualifications', 'experience_years', 'skills'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_hired': forms.DateInput(attrs={'type': 'date'}),
        }


class NonStaffForm(forms.ModelForm):
    class Meta:
        model = NonStaff
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth',
            'gender', 'national_id', 'passport_number', 'photo', 'role',
            'department', 'assigned_supervisor', 'address',
            'emergency_contact_name', 'emergency_contact_phone', 'profile_picture'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['patient', 'date', 'description', 'file']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
