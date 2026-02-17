from django.contrib import admin

from account.models import Profile, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'birth_of_date', 'photo']
    raw_id_fields = ['user']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_from', 'user_to', 'created']


