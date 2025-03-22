from django.db import models
from django.utils.timezone import now


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Image(models.Model):

    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/', default='images/icons/icon-close.svg')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    time = models.DateField()
    time_end = models.DateField(default=now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.company

class Education(models.Model):
    school = models.CharField(max_length=255)
    graduate = models.CharField(max_length=255)
    time = models.DateField()
    time_end = models.DateField(default=now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.school

class Project(models.Model):
    project = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(default="https://example.com")
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.project

class PositionPerson(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name