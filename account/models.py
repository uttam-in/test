from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Doctor(models.Model):
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s %s %s " %(self.email, self.phone, self.password)


class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    birthdate = models.DateField(null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s %s %s" % (self.first_name, self.last_name, self.email, self.birthdate, self.doctor)


class Language(models.Model):
    language_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.language_name


class Diplomas(models.Model):
    diploma_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.diploma_name


class Profile(models.Model):
    birthdate = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    spoken_languages = ArrayField(models.IntegerField(null=False, blank=False))
    diplomas = ArrayField(models.IntegerField(null=False, blank=False))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/', null=False, blank=False)

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.birthdate, self.gender, self.location, self.spoken_languages,
                                      self.diplomas, self.picture)

