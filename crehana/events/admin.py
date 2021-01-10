from django.contrib import admin

from crehana.events.models import Event

class EventAdmin(admin.ModelAdmin):

    fields = ('event_type','minute','inscription')

    list_display=('event_type','minute','user','category','course','day')

    list_filter=("event_type",'day')

    list_per_page = 10

admin.site.register(Event, EventAdmin)