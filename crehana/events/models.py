from django.db import models
from crehana.gestion.models import Inscription
from datetime import datetime

EVENT_TYPE_CHOICES = [
    ('1', 'Inicio de video'),
    ('2', 'Pausa'),
    ('3', 'Reproducción'),
    ('4', 'Final del video'),
]

class Event(models.Model):
    class Meta:
        verbose_name_plural = "Video Event"
        db_table = "Event"

    event_type = models.CharField(max_length=1,verbose_name='Event type',choices=EVENT_TYPE_CHOICES)
    minute = models.IntegerField(verbose_name='Minute')
    inscription = models.ForeignKey(Inscription,on_delete=models.CASCADE,verbose_name='Inscription')
    day = models.DateTimeField(verbose_name="Day",default=datetime.now)
    
    def __str__(self):
        if int(self.event_type) <= 4:
            return "Evento: %s - Minuto: %s - Alumno: %s - Curso: %s" % (EVENT_TYPE_CHOICES[int(self.event_type) - 1][1], str(self.minute),self.inscription.user.email,self.inscription.course.title)
        else:
            return "Evento no encontrado"
    
    def category(self):
        return self.inscription.course.category.name

    def course(self):
        return self.inscription.course.title
    
    def user(self):
        return self.inscription.user.email
