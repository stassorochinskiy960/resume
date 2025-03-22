from django.contrib import admin
from .models import Image, Experience, Education, Project, PositionPerson


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'file', 'image']
    list_filter = ['title']

admin.site.register(Image, ImageAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'time', 'time_end', 'description']
    list_filter = ['company']

admin.site.register(Experience, ExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'graduate', 'time', 'time_end', 'description']
    list_filter = ['school']

admin.site.register(Education, EducationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project', 'title', 'description', 'image']
    list_filter = ['project']

admin.site.register(Project, ProjectAdmin)

class PositionPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'description', 'image']
    list_filter = ['name']

admin.site.register(PositionPerson, PositionPersonAdmin)
