from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date', 'completed')
    list_filter = ('priority', 'due_date', 'completed')
    search_fields = ('title', 'description')
