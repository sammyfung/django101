from django.contrib import admin
from .models import Event, Participant

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'start_time')
    list_filter = ['active']
    search_fields = ['code', 'name']


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'event', 'code')
    list_filter = ['event__name']
    search_fields = ['event__name', 'code', 'first_name', 'last_name', 'company', 'email', 'phone']


admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
