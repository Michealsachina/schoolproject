from django.db import models
from myproject.school.models import School
from datetime import date

class Student(models.Model):
    GRADE_CHOICES = [
        ('O', 'O'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C', 'C'),
        ('Fail', 'Fail'),
        ('Absent', 'Absent'),
    ]

    student_name = models.CharField(max_length=100)
    dob = models.DateField()
    student_class = models.CharField(max_length=20)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, blank=True)  # ✅ dropdown
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to="student_photos/", blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.student_name

    @property
    def days(self):
        """Number of days since DOB until today"""
        if self.dob:
            return (date.today() - self.dob).days
        return 0
