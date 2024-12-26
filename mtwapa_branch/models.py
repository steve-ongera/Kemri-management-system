from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse



# Doctor Model
class Doctor(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True
    )
    phone = models.CharField(max_length=100)
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100)
    identification_no = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.ForeignKey(
        'Department', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='doctors'  # Custom related_name to avoid clash
    )
    years_of_experience = models.PositiveIntegerField()
    available_days = models.CharField(max_length=255)  # e.g., "Monday, Wednesday, Friday"
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


# Patient Model
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True
    )
    email = models.EmailField(max_length=100 , blank=True, null=True )
    Identification_no= models.CharField(max_length=100 , blank=True, null=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    chronic_conditions = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='patient_profiles/', blank=True, null=True)
    date_added = models.DateTimeField( blank=True, null=True )  # Automatically sets the date when a patient is added

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Intern Model
class Intern(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 , blank=True, null=True )
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True
    )
    Identification_no= models.CharField(max_length=100 , blank=True, null=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    assigned_area = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='intern_profiles/', blank=True, null=True)

    def __str__(self):
        return f"Intern {self.first_name} {self.last_name}"


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    head = models.OneToOneField(
        Doctor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='headed_department'  # Custom related_name
    )
    # Contact Information
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    research_focus = models.TextField(blank=True, null=True)  # Specific areas of research
   


    def __str__(self):
        return self.name


# Appointment Model
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='scheduled'
    )

    def __str__(self):
        return f"Appointment with Dr.  {self.doctor.first_name} {self.doctor.last_name} on {self.date}"


# Medical Record Model
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    visit_reason = models.CharField(max_length=255, blank=True, null=True)  # Reason for visit

    # Clinical Details
    diagnosis = models.TextField()  # Diagnosis details
    symptoms = models.TextField(blank=True, null=True)  # Symptoms reported by the patient
    physical_examination = models.TextField(blank=True, null=True)  # Doctor's observations during examination
    vital_signs = models.CharField(max_length=255, blank=True, null=True)  # Example: "Temp: 37.5°C, BP: 120/80"

    # Test Details
    tests_ordered = models.TextField(blank=True, null=True)  # Tests requested by the doctor
    test_results = models.TextField(blank=True, null=True)  # Results of tests conducted

    # Treatment Details
    prescription = models.TextField(blank=True, null=True)  # Medications prescribed
    procedures = models.TextField(blank=True, null=True)  # Any procedures performed
    follow_up_date = models.DateField(blank=True, null=True)  # Next scheduled visit

    # Notes
    additional_notes = models.TextField(blank=True, null=True)  # Any additional observations or instructions

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medical Record for  {self.patient.first_name} {self.patient.last_name} on {self.date}"



# Staff Model


class Staff(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True, null=True)
    identification_no = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True
    )
    profile_picture = models.ImageField(upload_to='staff_profiles/', blank=True, null=True)

    # Employment Details
    position = models.CharField(max_length=100)  # E.g., Researcher, Lab Technician
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    employee_id = models.CharField(max_length=50, unique=True)  # Unique employee ID
    date_hired = models.DateField(default=now)
    contract_type = models.CharField(
        max_length=50,
        choices=[('Permanent', 'Permanent'), ('Contract', 'Contract'), ('Intern', 'Intern')],
        blank=True,
        null=True
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shift = models.CharField(
        max_length=50,
        choices=[('Day', 'Day'), ('Night', 'Night'), ('Flexible', 'Flexible')],
        blank=True,
        null=True
    )

    # Address Information
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)

    # Permissions and Access
    access_level = models.CharField(
        max_length=50,
        choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Staff', 'Staff')],
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    # Professional Information
    qualifications = models.TextField(blank=True, null=True)  # E.g., Degrees, Certifications
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)  # E.g., Specializations

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"





class NonStaff(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)  # Optional
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True
    )

    # Identification
    national_id = models.CharField(max_length=20, unique=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)  # Optional
    photo = models.ImageField(upload_to='nonstaff_photos/', blank=True, null=True)

    # Role and Purpose
    role = models.CharField(max_length=100, blank=True, null=True)  # E.g., Volunteer, Contractor, Visitor
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_supervisor = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)  # Optional

    # Additional Information
    address = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='non_staff_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

# Report Model
class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return f"Report for {self.patient.last_name} on {self.date}"
    
    def get_file_name(self):
        return self.file.name.split('/')[-1]

    def get_file_url(self):
        return self.file.url


# Lab Test Model
class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    results = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Lab Test: {self.test_name} for {self.patient.last_name}"
    
    def get_test_date_formatted(self):
        return self.test_date.strftime('%B %d, %Y')

    def get_test_summary(self):
        return self.results[:50] + '...' if self.results else "No results available"


#profile model 
class Profile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Staff', 'staff'),
        
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Staff')
    full_names = models.CharField(max_length=200)
    Region = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_names    


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # User performing the action
    action = models.CharField(max_length=255)  # The action performed
    timestamp = models.DateTimeField(default=now)  # Time of the activity
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Optional: Track user's IP address

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
    


class NewsUpdate(models.Model):
    CATEGORY_CHOICES = [
        ('KEMRI', 'KEMRI'),
        ('Health Staff', 'Health Staff'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='news_updates/', blank=True, null=True)
    published_date = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)  # Link to User

    def __str__(self):
        return self.title