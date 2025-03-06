from django.contrib import admin
from lesTaches.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','closed','colored_due_date')
    readonly_fields = ('created_date',)   
admin.site.register(Task, TaskAdmin) 