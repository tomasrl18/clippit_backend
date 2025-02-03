from django.contrib import admin
from .models import Note, Task

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'user')  # Campos visibles en la lista
    #search_fields = ('title', 'content')           # Búsqueda por estos campos
    #list_filter = ('created_at',)                  # Filtros disponibles

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'due_date', 'user')
    #search_fields = ('title', 'description')
    #list_filter = ('completed', 'due_date')