# core/models.py

from django.db import models
# Importamos el CustomUser para las relaciones, si las hubiera en el futuro
from users.models import CustomUser

class Nationalities(models.Model):
    nationality_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'olympus"."nationalities'
        verbose_name_plural = "Nationalities"

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    min_age = models.IntegerField(null=True, blank=True)
    max_age = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'olympus"."categories'
        verbose_name_plural = "Categories"

class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'olympus"."clubs'
        verbose_name_plural = "Clubs"

class Disciplines(models.Model):
    discipline_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'olympus"."disciplines'
        verbose_name_plural = "Disciplines"

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'olympus"."events'
        verbose_name_plural = "Events"

class Coaches(models.Model):
    coach_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'olympus"."coaches'
        verbose_name_plural = "Coaches"

class Athletes(models.Model):
    athlete_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    nationality = models.ForeignKey(Nationalities, on_delete=models.SET_NULL, null=True, blank=True, db_column='nationality_id')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True, db_column='category_id')
    club = models.ForeignKey(Clubs, on_delete=models.SET_NULL, null=True, blank=True, db_column='club_id')

    class Meta:
        db_table = 'olympus"."athletes'
        verbose_name_plural = "Athletes"

class Participations(models.Model):
    participation_id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athletes, on_delete=models.CASCADE, db_column='athlete_id', related_name='participations')
    event = models.ForeignKey(Events, on_delete=models.CASCADE, db_column='event_id')
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE, db_column='discipline_id')
    result = models.CharField(max_length=100, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'olympus"."participations'
        verbose_name_plural = "Participations"

class Trainings(models.Model):
    training_id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athletes, on_delete=models.CASCADE, db_column='athlete_id', related_name='trainings')
    coach = models.ForeignKey(Coaches, on_delete=models.CASCADE, db_column='coach_id')
    date = models.DateField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    training_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'olympus"."trainings'
        verbose_name_plural = "Trainings"

class Injuries(models.Model):
    injury_id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athletes, on_delete=models.CASCADE, db_column='athlete_id', related_name='injuries')
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    estimated_duration_days = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'olympus"."injuries'
        verbose_name_plural = "Injuries"

class MedicalHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athletes, on_delete=models.CASCADE, db_column='athlete_id', related_name='medical_history')
    date = models.DateField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'olympus"."medical_history'
        verbose_name_plural = "Medical Histories"