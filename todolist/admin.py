from django.contrib import admin
from todolist.models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'completed'
    list_editable = 'completed',
    list_display_links = 'title',
    search_fields = 'id', 'title',
    list_per_page = 10
    ordering = '-id',
    readonly_fields = 'created_at', 'completed_at', 'owner'