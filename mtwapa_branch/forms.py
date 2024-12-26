# forms.py
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')
        
        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        return user


class CustomUserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'first_name', 'last_name', 'gender', 'phone', 'emergency_contact_name',
            'emergency_contact_phone', 'address', 'identification_no', 'specialization',
            'department', 'years_of_experience', 'available_days', 'profile_picture'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Gender'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Name'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'identification_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identification No'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specialization'}),
            'department': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Department'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'available_days': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Available Days'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


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

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['patient', 'doctor', 'test_name', 'test_date', 'results']
        widgets = {
            'test_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PatientSearchForm(forms.Form):
    search_query = forms.CharField(label="Search", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Patients'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image', 'full_names', 'about', 'role', 'Region', 
            'county', 'address', 'phone', 'email'
        ]



class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = NewsUpdate
        fields = ['title', 'description', 'category', 'image']  # Include relevant fields