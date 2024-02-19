from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.utils import timezone

class TipoPunto(models.Model):
    descripcion = models.CharField(db_column='nombre', max_length=80)
    
    def __str__(self) -> str:
        return self.tipopunto

class ParteCuerpo(models.Model):
    nombre = models.CharField( max_length=20 )

    def __str__(self) -> str:
        return self.nombre

    class Meta:        
        db_table = 'PARTE_CUERPO'

class CanalAcupuntura(models.Model):
    cvecanal = models.CharField(db_column='CveCanal', max_length=20, unique=True)
    nomcanal = models.CharField(db_column='NomCanal', max_length=80)
    trayecto = models.CharField(max_length=20, null=True, blank=True, default='Trayecto')
    nomchino = models.CharField( max_length=20, null=True, blank=True, default='nombre chino')
    traduccion = models.CharField( max_length=80, null=True, blank=True, default='traduccion')
    numtotalpuntos = models.CharField( max_length=20,null=True, blank=True, default='num')
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate', default=timezone.now)

    def __str__(self) -> str:
        return self.nomcanal

    class Meta:        
        db_table = 'CANAL_ACUPUNTURA'



class Enfermedad(models.Model):
    cveenfermedad = models.CharField(db_column='CveEnfermedad', max_length=80, unique=True)
    nomenfermedad = models.CharField(db_column='NomEnfermedad', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.nomenfermedad
    
    class Meta:        
        db_table = 'ENFERMEDAD'

class Sintoma(models.Model):
    sintoma = models.CharField(db_column='Sintoma', max_length=255, default="sintoma", unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.sintoma

    class Meta:        
        db_table = 'SINTOMA'



class PuntoAcupuntura(models.Model):
    cvepunto =  models.CharField(db_column='CvePunto', max_length=20, unique=True)  
    nompunto = models.CharField(db_column='NomPunto', max_length=80)
    nomchino = models.CharField(db_column='NomChino', max_length=300, default="chino")
    cvecanal = models.ForeignKey(CanalAcupuntura, models.DO_NOTHING)
    #partecuerpo = models.ForeignKey(ParteCuerpo, models.DO_NOTHING,  default=1)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.nompunto
    
    class Meta:        
        db_table = 'PUNTO_ACUPUNTURA'


class PuntoCaracteristicas(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    desccaracteristicas = RichTextField(db_column='DescCaracteristicas', verbose_name="Caracteristicas", blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.desccaracteristicas

    class Meta:        
        db_table = 'PUNTO_CARACTERISTICAS'


class PuntoDocumentos(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)     
    ligadocumento = models.FileField(upload_to="documentos_puntos",db_column='LigaDocumento', max_length=255, verbose_name="Documento", blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligadocumento

    class Meta:        
        db_table = 'PUNTO_DOCUMENTOS'


class PuntoEnfermedad(models.Model):
    punto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)    
    enfermedad = models.ForeignKey(Enfermedad, models.CASCADE)    
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.cveenfermedad
    
    class Meta:
        unique_together = ('punto', 'enfermedad')

    class Meta:        
        db_table = 'PUNTO_ENFERMEDAD'


class PuntoImagenes(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    ligaimagen = models.ImageField(upload_to='images_puntos',db_column='LigaImagen', max_length=255, blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligaimagen

    class Meta:        
        db_table = 'PUNTO_IMAGENES'


class PuntoImagenLocalizacion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    ligaimagen = models.CharField(db_column='LigaImagen', max_length=255, blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligaimagen
    
    class Meta:        
        db_table = 'PUNTO_IMAGEN_LOCALIZACION'


class PuntoLocalizacion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    desclocalizacion = RichTextField(db_column='DescLocalizacion', verbose_name="Localizacion", blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.desclocalizacion
    
    class Meta:        
        db_table = 'PUNTO_LOCALIZACION'


class PuntoSignificado(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    descsignificado = RichTextField(db_column='DescSignificado', verbose_name="Significado", blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.descsignificado
    
    class Meta:        
        db_table = 'PUNTO_SIGNIFICADO'


class PuntoSintomatologia(models.Model):
    punto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    sintoma = models.ForeignKey(Sintoma, models.DO_NOTHING,  null=False)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)


    def __str__(self) -> str:
        return self.nomorgpartecuerpo   
     
    class Meta:
        unique_together = ('punto', 'sintoma')
    
    class Meta:        
        db_table = 'PUNTO_SINTOMATOLOGIA'


class PuntoVideos(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    ligavideo = models.CharField(db_column='LigaVideo', max_length=255, blank=True, unique=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligavideo
    
    class Meta:        
        db_table = 'PUNTO_VIDEOS'



class Sintomatologia(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    nomorgpartecuerpo = models.ForeignKey(ParteCuerpo, models.DO_NOTHING)
    sintoma = models.ForeignKey(Sintoma, models.DO_NOTHING)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.sintoma
    
    class Meta:        
        db_table = 'SINTOMATOLOGIA'


# Parte de cuerpo y emocion

class Emocion(models.Model):
    nombre = models.CharField( max_length=80, default='emocion')

    def __str__(self) -> str:
        return self.nombre

class CanalEmocion(models.Model):
    canal = models.ForeignKey(CanalAcupuntura, models.CASCADE)
    emocion = models.ForeignKey(Emocion, models.CASCADE)

class Elementos(models.Model):
    nombre = models.CharField( max_length=30, default='', unique=True)
    descripcion = models.CharField( max_length=240, default='')
    
    def __str__(self) -> str:
        return self.nombre

class CanalElemento(models.Model):
    canal = models.ForeignKey(CanalAcupuntura, models.CASCADE)
    elemento = models.ForeignKey(Elementos, models.CASCADE)


# Modelos para la tabla de elementos
    
class CategoriaElemento(models.Model):
    nombre = models.CharField( max_length=80, default='', unique=True)
    
    def __str__(self) -> str:
        return self.nombre

class ValoresElemento(models.Model):
    nombre = models.CharField( max_length=80, default='', unique=True)
        
    def __str__(self) -> str:
        return self.nombre

class TablaElemento(models.Model):
    tipo = models.ForeignKey(Elementos, models.DO_NOTHING)
    categoria = models.ForeignKey(CategoriaElemento, models.DO_NOTHING)
    valor = models.ForeignKey(ValoresElemento, models.DO_NOTHING)
    
    class Meta:
        unique_together = ('tipo', 'categoria', 'valor')