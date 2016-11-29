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
    course_number = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=45)
    department = models.ForeignKey('Department', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Course'


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
    semester_name = models.ForeignKey('Semester', models.DO_NOTHING, db_column='semester_name')
    meeting_days = models.CharField(max_length=5)
    meeting_start_time = models.TimeField()
    meeting_end_time = models.TimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Enrollment'
        unique_together = (('id', 'meeting_days'),)


class Project(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    course_number = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_number', blank=True, null=True)
    community_partner = models.ForeignKey(CommunityPartner, models.DO_NOTHING)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Project'


class Record(models.Model):
    enrollment = models.ForeignKey(Enrollment, models.DO_NOTHING)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    total_hours = models.DecimalField(max_digits=4, decimal_places=2)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.ForeignKey('RecordCategory', models.DO_NOTHING)
    is_active = models.IntegerField(blank=True, null=True)
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


class Semester(models.Model):
    name = models.CharField(unique=True, max_length=8)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Semester'


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=100)

