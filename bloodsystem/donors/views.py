from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    contact = models.CharField(max_length=100)
    eligibility = models.BooleanField(default=True)
    last_donation = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class BloodRequest(models.Model):
    hospital_name = models.CharField(max_length=200)
    blood_type_needed = models.CharField(max_length=3)
    quantity = models.IntegerField()
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

