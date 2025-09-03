from django.contrib import admin
from .models import Client, Deal, Task

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'company', 'created_at')
    search_fields = ('name', 'email', 'company')
    list_filter = ('created_at',)

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'amount', 'status', 'created_at', 'close_date')
    search_fields = ('title', 'client__name')
    list_filter = ('status', 'created_at', 'close_date')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'priority', 'done', 'due_date', 'created_at')
    search_fields = ('title', 'client__name')
    list_filter = ('priority', 'done', 'due_date', 'created_at')
