from django.contrib import admin

# Register your models here.
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name','email', 'date_of_birth', 'education_field', 'degree', 'university', 'graduation_year']