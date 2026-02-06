# school/models.py

from django.db import models

class School(models.Model):
    school_name = models.CharField("School Name", max_length=200)
    address = models.TextField("Address", blank=True, null=True)
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", max_length=100)
    pincode = models.CharField("Pincode", max_length=10, blank=True, null=True)
    principal_name = models.CharField("Principal Name", max_length=100, blank=True, null=True)
    phone = models.CharField("Phone", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    established_year = models.PositiveIntegerField("Established Year", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name
