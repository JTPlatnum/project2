from django.contrib import admin
from favorites.models import Favorites

#admin.site.register(Favorites)

class Favorites_Admin(admin.ModelAdmin):
    fields = ['user', 'program_id', 'created_at', 'updated_at']           
admin.site.register(Favorites, Favorites_Admin)

