from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Intern)
admin.site.register(Department)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Staff)
admin.site.register(NonStaff)
admin.site.register(Report)
admin.site.register(LabTest)
admin.site.register(Profile)
admin.site.register(Activity)
