from django.contrib.auth.models import User
from django.db import models

class Instructor(models.Model):
    """An instructor.....
    THIS IS JUST AN EXAMPLE, PLEASE REPLACE

    Attributes:
        created (DateTime): Time instructor created.
        owner (User): The user that is the instructor.

    """
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructors')

    class Meta:
        ordering = ('created',)

class Course(models.Model):
    """A course.....
    THIS IS JUST AN EXAMPLE, PLEASE REPLACE

    Attributes:
        created (DateTime): The time this course was created.
        owner (User): The user(s) in the couse.
        instructor (Instructors): ...
        ispositive (Boolean): Example boolean field......

    """
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    is_positive = models.BooleanField()

    class Meta:
        ordering = ('created',)
