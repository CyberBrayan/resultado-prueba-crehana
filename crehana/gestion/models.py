from django.db import models
from django.conf import settings
from crehana.curso.models import Course

class Inscription(models.Model):
    class Meta:
        verbose_name_plural = "Inscription"
        db_table = "Inscription"

    user =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='User')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='Course')
    
    def __str__(self):

        return "Inscripción del alumno: %s en el curso de %s - Categoría: %s" % (self.user.email,self.course.title,self.course.category.name)

class VideoProgress(models.Model):
    class Meta:
        verbose_name_plural = "Video progress"
        db_table = "video_progress"

    minute_r_d = models.IntegerField(verbose_name='Minutes of daily playback')
    inscription = models.ForeignKey(Inscription,on_delete=models.CASCADE,verbose_name='Inscription')
    day = models.DateField(verbose_name="Day", blank=False,null=False)
    
    def __str__(self):
        return "Curso: %s - Alumno: %s - Día: %s - Progreso: %s minutos" % (self.inscription.course.title,self.inscription.user.email,str(self.day),str(self.minute_r_d))
    
    def category(self):
        return self.inscription.course.category.name

    def course(self):
        return self.inscription.course.title
    
    def user(self):
        return self.inscription.user.email