from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, ResetCode

# Register your models here.


admin.site.register(Student, UserAdmin)
admin.site.register(ResetCode)