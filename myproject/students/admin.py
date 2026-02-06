from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'dob', 'student_class', 'grade', 'school')
    list_filter = ('grade', 'school')
    search_fields = ('student_name', 'email')
