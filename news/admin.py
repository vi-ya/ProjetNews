from django.contrib import admin
from .models import New

class NewsAdmin(admin.ModelAdmin):
    list_display = ('photo', 'section','title','description', 'source', 'author','website', 'date', 'publicationdate')

admin.site.register(New)
