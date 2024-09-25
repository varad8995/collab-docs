from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Document, Collaborator

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username')
    list_filter = ('created_at', 'updated_at')

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'role')
    search_fields = ('user__username', 'document__title')
    list_filter = ('role',)
