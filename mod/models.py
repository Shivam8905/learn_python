from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.IntegerField(unique=True)

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    duration = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=50)
    college = models.ForeignKey(College, on_delete = models.PROTECT)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    course = models.ForeignKey(Course, on_delete = models.PROTECT)

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

class staff(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    college = models.ForeignKey(College, on_delete = models.PROTECT)
    role = models.ForeignKey(Role, on_delete = models.PROTECT)




