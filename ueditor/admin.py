from django.contrib import admin
from .models import UeditorFile


class UeditorFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UeditorFile, UeditorFileAdmin)
