from django.contrib import admin
from .models import Module


class ModuleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'number', 'name', 'description', 'slug',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'description',)
    list_filter = ('name',)


admin.site.register(Module, ModuleAdmin)
