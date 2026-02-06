from django.urls import path
from . import views

urlpatterns = [
    path('', views.school_list, name='school_list'),
    path('add/', views.add_school, name='add_school'),
    path('edit/<int:pk>/', views.edit_school, name='edit_school'),
    path('delete/<int:pk>/', views.delete_school, name='delete_school'),
    path('<int:pk>/', views.school_detail, name='school_detail'),
    path('students/add/<int:school_id>/', views.add_student, name='add_student'),
]
