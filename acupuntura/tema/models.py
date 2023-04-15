from django.db import models
from simple_history.models import HistoricalRecords
from colorfield.fields import ColorField

# Create your models here.
class parametros_colores(models.Model):
    elemento = models.CharField(db_column='elemento', max_length=50, blank=False, null=False)
    color = ColorField(default='#FF0000')

    class Meta:
        db_table = 'parametros_colores'

class parametros_imagenes(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    image = models.ImageField(upload_to='images_parameter')

    def __str__(self):
        return self.title