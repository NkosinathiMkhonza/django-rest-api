from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ['id', 'title', 'tech_stack', 'status', 'created_at']
    list_filter   = ['status']
    search_fields = ['title', 'tech_stack']
    ordering      = ['-created_at']