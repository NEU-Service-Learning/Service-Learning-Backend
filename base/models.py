# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class College(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'College'


class CommunityPartner(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Community_Partner'


class Course(models.Model):
    course_number = models.CharField(max_length=8)
    name = models.CharField(max_length=45)
    semester_id = models.CharField(max_length=8)
    department = models.ForeignKey('Department', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Course'
        unique_together = (('course_number', 'semester_id'),)


class Department(models.Model):
    id = models.ForeignKey(College, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=45)
    college_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Department'


class Enrollment(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    course_number = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_number')
    current_class = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Enrollment'
        unique_together = (('user', 'course_number'),)


class Project(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    community_partner = models.ForeignKey(CommunityPartner, models.DO_NOTHING)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Project'


class Record(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    course_number = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_number')
    project = models.ForeignKey(Project, models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    total_hours = models.DecimalField(max_digits=4, decimal_places=2)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.ForeignKey('RecordCategory', models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    extra_field = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Record'


class RecordCategory(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Record_Category'
