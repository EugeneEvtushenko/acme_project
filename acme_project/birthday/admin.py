from django.contrib import admin

from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )
    list_editable = (
    )
    search_fields = ('tag',)
    list_filter = ('tag',)


admin.site.empty_value_display = 'Не задано'
