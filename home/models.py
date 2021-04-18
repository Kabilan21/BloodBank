from django.db import models


class BloodData(models.Model):
    name = models.CharField(max_length=120)
    DOB = models.DateField()
    email = models.CharField(max_length=120)
    number = models.CharField(max_length=18)
    blood_choice = (('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'),
                    ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'))
    bloodgroup = models.CharField(
        max_length=10, choices=blood_choice, null=False)
    location = models.CharField(max_length=120)
    receive_mail = models.BooleanField(default=True)
    show_onsearch = models.BooleanField(default=True)
    unique_ID = models.CharField(max_length=120)
    more_location = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.pk}"


class Bloodlength(models.Model):
    O_negative = models.IntegerField()
    O_positive = models.IntegerField()
    A_negative = models.IntegerField()
    A_positive = models.IntegerField()
    B_negative = models.IntegerField()
    B_positive = models.IntegerField()
    AB_negative = models.IntegerField()
    AB_positive = models.IntegerField()

    def __str__(self):
        return f"{self.pk}"


class BloodNeed(models.Model):
    patient_name = models.CharField(max_length=120)
    attender_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    number = models.CharField(max_length=14)
    blood_choice = (('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'),
                    ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'))
    bloodgroup = models.CharField(
        max_length=10, choices=blood_choice, null=False)
    blood_units = models.IntegerField(default=1)
    hospital_name = models.CharField(max_length=210)
    location = models.CharField(max_length=420)
    can_afford_travel = models.BooleanField(null=True, default=False)
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}"
