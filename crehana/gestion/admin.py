from django.contrib import admin

from crehana.gestion.models import Inscription,VideoProgress

class InscriptionAdmin(admin.ModelAdmin):

    fields = ('user','course',)

    list_display=("user",'course')

    search_fields=("user",'course')

    list_per_page = 10

class VideoProgressAdmin(admin.ModelAdmin):

    fields = ('minute_r_d','inscription','day')

    list_display=('minute_r_d','user','course','category','day')

    search_fields=('inscription',)

    list_filter=('day',)

    list_per_page = 10

admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(VideoProgress, VideoProgressAdmin)