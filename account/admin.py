from django.contrib import admin
from .models import Patient, Doctor, Language, Diplomas, Profile
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Language)
admin.site.register(Diplomas)
admin.site.register(Profile)
