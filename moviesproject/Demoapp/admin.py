from django.contrib import admin
from Demoapp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
     list_display = ['id','rdate','mname','actor','actress','ratings']

admin.site.register(Movie,MovieAdmin)
