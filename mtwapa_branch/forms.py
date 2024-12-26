# forms.py
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime  # Add this import for datetime

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
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Gender'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Identification_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identification Number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Name'}),
            'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Number'}),
            'blood_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blood Type'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Allergies', 'rows': 3}),
            'chronic_conditions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Chronic Conditions', 'rows': 3}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Medical History', 'rows': 3}),
            'insurance_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insurance Provider'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }



class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'emergency_contact_name',
            'emergency_contact_phone', 'gender', 'Identification_no', 'assigned_doctor',
            'assigned_area', 'start_date', 'end_date', 'profile_picture'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Name'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Gender'}),
            'Identification_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identification Number'}),
            'assigned_doctor': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Assigned Doctor'}),
            'assigned_area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assigned Area'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Start Date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'End Date'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }




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
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder': 'Select date and time'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter reason for appointment'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

   
    
    # Optional method to add custom widgets or classes to other fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally add placeholder or styles dynamically to each field
        self.fields['patient'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select Patient'})
        self.fields['doctor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select Doctor'})

    # Add custom error messages if needed
    def add_error_messages(self):
        for field in self.fields:
            self.fields[field].error_messages = {
                'required': f"{field} is a mandatory field.",
                'invalid': f"Invalid {field} entered.",
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


from django import forms
from .models import Staff

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
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'identification_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identification No'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Gender'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
            'date_hired': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contract_type': forms.Select(attrs={'class': 'form-select'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'shift': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shift'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Name'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Phone'}),
            'access_level': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'qualifications': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Qualifications', 'rows': 3}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Skills', 'rows': 3}),
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
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter national ID'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter passport number'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter role'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'assigned_supervisor': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter emergency contact name'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter emergency contact phone'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['patient', 'date', 'description', 'file']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['patient', 'doctor', 'test_name', 'test_date', 'results']
        widgets = {
            'test_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'test_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Test Name'}),
            'results': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Test Results'}),
        }


class PatientSearchForm(forms.Form):
    search_query = forms.CharField(label="Search", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Patients'}))

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image', 'full_names', 'about', 'role', 'Region', 
            'county', 'address', 'phone', 'email'
        ]
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'full_names': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full names'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write about yourself'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'Region': forms.Select(attrs={'class': 'form-control'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter county'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'})
        }
        labels = {
            'profile_image': 'Profile Image',
            'full_names': 'Full Names',
            'about': 'About Me',
            'role': 'Role',
            'Region': 'Region',
            'county': 'County',
            'address': 'Address',
            'phone': 'Phone Number',
            'email': 'Email Address'
        }
        help_texts = {
            'email': 'Please enter a valid email address.'
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email




class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = NewsUpdate
        fields = ['title', 'description', 'category', 'image']  # Include relevant fields