# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncDay
from datetime import datetime, timedelta
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.db.models import Count
from datetime import datetime
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json


@login_required
def dashboard(request):
    data = DiseaseTest.objects.values('disease_name', 'test_count')
    serialized_data = json.dumps(list(data), cls=DjangoJSONEncoder)
    # Get the current year
    current_year = datetime.now().year

    # Query for male and female patients grouped by the month they were added
    gender_counts = Patient.objects.filter(date_added__year=current_year).values('gender', 'date_added__month').annotate(count=Count('id')).order_by('date_added__month')

    # Prepare data for the chart
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    male_data = [0] * 12
    female_data = [0] * 12

    # Fill the male and female data arrays based on the query results
    for record in gender_counts:
        month = record['date_added__month'] - 1  # Adjusting to 0-based index for months
        if record['gender'] == 'Male':
            male_data[month] = record['count']
        elif record['gender'] == 'Female':
            female_data[month] = record['count']


    # Date ranges
    
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()[:6]
    recent_activities = Activity.objects.order_by('-timestamp')[:6]
    news_updates = NewsUpdate.objects.all().order_by('-published_date')[:7]
    
    # Basic stats
    context = {
        'total_doctors': Doctor.objects.count(),
        'total_patients': Patient.objects.count(),
        'total_staff': Staff.objects.count(),
        'total_appointments': Appointment.objects.filter(status='scheduled').count(),
        'total_departments': Department.objects.count(),
        'doctors': doctors,
        'patients':patients,
        'recent_activities':recent_activities,
        'news_updates': news_updates,
        #graph
        'months': months,
        'male_data': male_data,
        'female_data': female_data,
        'data': serialized_data,  # Pass the serialized data
    }
    
    
    
    # Department distribution
    dept_distribution = (Doctor.objects
        .values('department__name')
        .annotate(count=Count('id'))
        .order_by('-count'))
    
    # Patient growth
    patient_growth = (Patient.objects
        .annotate(month=TruncMonth('date_of_birth'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month'))
    
    # Add chart data to context
    context.update({
        
        'department_data': list(dept_distribution),
        'patient_growth_data': list(patient_growth),
        'recent_appointments': Appointment.objects.select_related('doctor', 'patient').order_by('-date')[:5],
    })
    
    return render(request, 'admin/dashboard.html', context)


# List view
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

# Detail view
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})

# Create view
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_form.html', {'form': form})

# Update view
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor/update_doctor.html', {'form': form})

# Delete view
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor/doctor_confirm_delete.html', {'doctor': doctor})

#search  doctor 
def search_doctors(request):
   query = request.GET.get('q')
   doctors = Doctor.objects.all()
   
   if query:
       doctors = doctors.filter(
           Q(first_name__icontains=query) |
           Q(last_name__icontains=query) |
           Q(specialization__icontains=query) |
           Q(department__name__icontains=query)
       )
   
   return render(request, 'doctor/search.html', {'doctors': doctors})


# List view
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})

# Detail view
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

# Create view
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_form.html', {'form': form})

# Update view
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/patient_form.html', {'form': form})

# Delete view
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient/patient_confirm_delete.html', {'patient': patient})
#search for patient 

def patient_search(request):
    form = PatientSearchForm(request.GET)
    patients = []

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            # Using Q objects to create a logical OR condition
            patients = Patient.objects.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(Identification_no__icontains=search_query) |
                Q(email__icontains=search_query)
            )

    return render(request, 'patient/patient_search.html', {'form': form, 'patients': patients})


# List view
def intern_list(request):
    interns = Intern.objects.all()
    return render(request, 'intern/intern_list.html', {'interns': interns})

# Detail view
def intern_detail(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    return render(request, 'intern/intern_detail.html', {'intern': intern})

# Create view
def intern_create(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('intern_list')
    else:
        form = InternForm()
    return render(request, 'intern/intern_form.html', {'form': form})

# Update view
def intern_update(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')
    else:
        form = InternForm(instance=intern)
    return render(request, 'intern/intern_form.html', {'form': form})

# Delete view
def intern_delete(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    if request.method == 'POST':
        intern.delete()
        return redirect('intern_list')
    return render(request, 'intern/intern_confirm_delete.html', {'intern': intern})



# List view
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

# Detail view
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'department/department_detail.html', {'department': department})

# Create view
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department/department_form.html', {'form': form})

# Update view
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department/department_form.html', {'form': form})

# Delete view
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department/department_confirm_delete.html', {'department': department})

# List view
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/appointment_list.html', {'appointments': appointments})

# Detail view
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment/appointment_detail.html', {'appointment': appointment})

# Create view
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/appointment_form.html', {'form': form})

# Update view
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment/appointment_form.html', {'form': form})

# Delete view
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment/appointment_confirm_delete.html', {'appointment': appointment})


# List View
def medical_record_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'medical_record/medical_record_list.html', {'records': records})

# Detail View
def medical_record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'medical_record/medical_record_detail.html', {'record': record})

# Create View
def medical_record_create(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_record/medical_record_form.html', {'form': form})

# Update View
def medical_record_update(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, 'medical_record/medical_record_form.html', {'form': form})

# Delete View
def medical_record_delete(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('medical_record_list')
    return render(request, 'medical_record/medical_record_confirm_delete.html', {'record': record})



# List View
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members})

# Detail View
def staff_detail(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/staff_detail.html', {'staff_member': staff_member})

# Create View
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/staff_form.html', {'form': form})

# Update View
def staff_update(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff_member)
    return render(request, 'staff/staff_form.html', {'form': form})

# Delete View
def staff_delete(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff_member.delete()
        return redirect('staff_list')
    return render(request, 'staff/staff_confirm_delete.html', {'staff_member': staff_member})



# List View
def nonstaff_list(request):
    nonstaff_members = NonStaff.objects.all()
    return render(request, 'nonstaff/nonstaff_list.html', {'nonstaff_members': nonstaff_members})

# Detail View
def nonstaff_detail(request, pk):
    nonstaff_member = get_object_or_404(NonStaff, pk=pk)
    return render(request, 'nonstaff/nonstaff_detail.html', {'nonstaff_member': nonstaff_member})

# Create View
def nonstaff_create(request):
    if request.method == 'POST':
        form = NonStaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nonstaff_list')
    else:
        form = NonStaffForm()
    return render(request, 'nonstaff/nonstaff_form.html', {'form': form})

# Update View
def nonstaff_update(request, pk):
    nonstaff_member = get_object_or_404(NonStaff, pk=pk)
    if request.method == 'POST':
        form = NonStaffForm(request.POST, request.FILES, instance=nonstaff_member)
        if form.is_valid():
            form.save()
            return redirect('nonstaff_list')
    else:
        form = NonStaffForm(instance=nonstaff_member)
    return render(request, 'nonstaff/nonstaff_form.html', {'form': form})

# Delete View
def nonstaff_delete(request, pk):
    nonstaff_member = get_object_or_404(NonStaff, pk=pk)
    if request.method == 'POST':
        nonstaff_member.delete()
        return redirect('nonstaff_list')
    return render(request, 'nonstaff/nonstaff_confirm_delete.html', {'nonstaff_member': nonstaff_member})



# List View
def report_list(request):
    reports = Report.objects.all().order_by('-date')
    return render(request, 'report/report_list.html', {'reports': reports})

# Detail View
def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report/report_detail.html', {'report': report})

# Create View
def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'report/report_form.html', {'form': form})

# Update View
def report_update(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'report/report_form.html', {'form': form})

# Delete View
def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'report/report_confirm_delete.html', {'report': report})



# List View
def labtest_list(request):
    tests = LabTest.objects.all().order_by('-test_date')
    return render(request, 'labtest/labtest_list.html', {'tests': tests})

# Detail View
def labtest_detail(request, pk):
    test = get_object_or_404(LabTest, pk=pk)
    return render(request, 'labtest/labtest_detail.html', {'test': test})

# Create View
def labtest_create(request):
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labtest_list')
    else:
        form = LabTestForm()
    return render(request, 'labtest/labtest_form.html', {'form': form})

# Update View
def labtest_update(request, pk):
    test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        form = LabTestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('labtest_list')
    else:
        form = LabTestForm(instance=test)
    return render(request, 'labtest/labtest_form.html', {'form': form})

# Delete View
def labtest_delete(request, pk):
    test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        test.delete()
        return redirect('labtest_list')
    return render(request, 'labtest/labtest_confirm_delete.html', {'test': test})


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a protected page or admin dashboard after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomUserLoginForm()

    return render(request, 'auth/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# View to display the help and support page
def help_and_support(request):
    return render(request, 'help/help_and_support.html')


# View to display the system settings page
def system_settings(request):
    return render(request, 'help/system_settings.html')


@login_required
def profile_detail(request):
    try:
        # Get or create the user's profile
        profile, created = Profile.objects.get_or_create(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save the form with the new image
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'auth/profile_detail.html', {
        'profile': profile,
        'form': form,
    })


@login_required
def create_profile(request):
    # Check if the logged-in user already has a profile
    if hasattr(request.user, 'profile'):
        return redirect('profile_detail')  # If the user already has a profile, redirect to profile detail

    # Handle the form submission
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associate the profile with the logged-in user
            profile.save()
            return redirect('profile_detail')  # Redirect to profile detail after saving

    else:
        form = ProfileForm()

    return render(request, 'auth/create_profile.html', {'form': form})


@login_required
def edit_profile(request):
    # Get the user's profile
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Bind the form to the POST data
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Save the updated profile
            form.save()
            return redirect('profile_detail')  # Redirect to the profile page after saving
    else:
        # Create an empty form bound to the current profile
        form = ProfileForm(instance=profile)

    return render(request, 'auth/edit_profile.html', {'form': form})


@login_required
def news_edit(request, pk):
    news = get_object_or_404(NewsUpdate, pk=pk)

    # Ensure only the creator can edit
    if news.created_by != request.user:
        return redirect('dashboard')  # Redirect to a suitable page, e.g., the home page

    if request.method == 'POST':
        form = NewsUpdateForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a suitable page after editing
    else:
        form = NewsUpdateForm(instance=news)

    return render(request, 'news/news_edit.html', {'form': form})


@login_required
def news_delete(request, pk):
    news = get_object_or_404(NewsUpdate, pk=pk)

    # Ensure only the creator can delete
    if news.created_by != request.user:
        return HttpResponseForbidden("You are not allowed to delete this news item.")

    if request.method == 'POST':  # Confirm deletion via POST request
        news.delete()
        return redirect('dashbaord')  # Redirect to a suitable page after deletion

    return render(request, 'news/news_confirm_delete.html', {'news': news})