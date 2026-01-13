from django.contrib import admin
from .models import Cities, Tourism, TripPlanner, CultureAndTradition, Food

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

@admin.register(Tourism)
class TourismAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'id')
    list_filter = ('city',)
    search_fields = ('name', 'location', 'about')

@admin.register(TripPlanner)
class TripPlannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'tourism', 'contact_person_name', 'mobile', 'id')
    list_filter = ('tourism',)
    search_fields = ('name', 'contact_person_name', 'mobile')

@admin.register(CultureAndTradition)
class CultureAndTraditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'about')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'about')
