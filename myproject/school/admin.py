from django.contrib import admin
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name','city','state','principal_name','phone','email','established_year')
    search_fields = ('school_name','city','principal_name')
    list_filter = ('state','established_year')  # ✅ adds filters in right sidebar
