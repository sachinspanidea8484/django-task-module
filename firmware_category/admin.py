from django.contrib import admin
from .models import FirmwareCategory

@admin.register(FirmwareCategory)
class FirmwareCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status')
