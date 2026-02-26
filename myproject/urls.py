# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # returns the splash home page (we'll create home.html)
    return render(request, "home.html")


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('schools/', include('school.urls')),
    path('students/', include('students.urls')),
]
