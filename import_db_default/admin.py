from django.contrib.admin import register, ModelAdmin
from import_export.admin import ImportExportMixin
from .models import Item

@register(Item)
class ItemAdmin(ImportExportMixin, ModelAdmin):
    list_display = ["name", "created"]
