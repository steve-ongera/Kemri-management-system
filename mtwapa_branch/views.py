# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
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
    return render(request, 'doctor/doctor_form.html', {'form': form})

# Delete view
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor/doctor_confirm_delete.html', {'doctor': doctor})


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
