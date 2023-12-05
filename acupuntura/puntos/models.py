from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.utils import timezone

class TipoPunto(models.Model):
    tipopunto = models.CharField(db_column='clave', max_length=20)
    descripciontipopunto = models.CharField(db_column='nombre', max_length=80)
    
    def __str__(self) -> str:
        return self.tipopunto

class ParteCuerpo(models.Model):
    nombre = models.CharField( max_length=20 )

    def __str__(self) -> str:
        return self.nombre

    class Meta:        
        db_table = 'PARTE_CUERPO'

class CanalAcupuntura(models.Model):
    cvecanal = models.CharField(db_column='CveCanal', max_length=20)
    nomcanal = models.CharField(db_column='NomCanal', max_length=80)
    trayecto = models.CharField(max_length=20, default=None)
    nomchino = models.CharField( max_length=20, default=None)
    traduccion = models.CharField( max_length=80, default=None)
    numtotalpuntos = models.CharField( max_length=20, default=None)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate', default=timezone.now)

    def __str__(self) -> str:
        return self.nomcanal

    class Meta:        
        db_table = 'CANAL_ACUPUNTURA'



class Enfermedad(models.Model):
    cveenfermedad = models.CharField(db_column='CveEnfermedad', max_length=20)
    nomenfermedad = models.CharField(db_column='NomEnfermedad', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.nomenfermedad
    
    class Meta:        
        db_table = 'ENFERMEDAD'

class Sintoma(models.Model):
    sintoma = models.CharField(db_column='Sintoma', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.sintoma

    class Meta:        
        db_table = 'SINTOMA'



class PuntoAcupuntura(models.Model):
    cvepunto =  models.CharField(db_column='CvePunto', max_length=20)  
    nompunto = models.CharField(db_column='NomPunto', max_length=80)
    nomlargopunto = models.CharField(db_column='NomLargoPunto', max_length=300)
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
    desccaracteristicas = RichTextField(db_column='DescCaracteristicas', verbose_name="Caracteristicas", blank=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.desccaracteristicas

    class Meta:        
        db_table = 'PUNTO_CARACTERISTICAS'


class PuntoDocumentos(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)     
    ligadocumento = models.FileField(upload_to="documentos_puntos",db_column='LigaDocumento', max_length=255, verbose_name="Documento", blank=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligadocumento

    class Meta:        
        db_table = 'PUNTO_DOCUMENTOS'


class PuntoEnfermedad(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)    
    cveenfermedad = models.ForeignKey(Enfermedad, models.CASCADE, blank=True)    
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.cveenfermedad

    class Meta:        
        db_table = 'PUNTO_ENFERMEDAD'


class PuntoImagenes(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    ligaimagen = models.ImageField(upload_to='images_puntos',db_column='LigaImagen', max_length=255, blank=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligaimagen

    class Meta:        
        db_table = 'PUNTO_IMAGENES'


class PuntoImagenLocalizacion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    ligaimagen = models.CharField(db_column='LigaImagen', max_length=255, blank=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.ligaimagen
    
    class Meta:        
        db_table = 'PUNTO_IMAGEN_LOCALIZACION'


class PuntoLocalizacion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    desclocalizacion = RichTextField(db_column='DescLocalizacion', verbose_name="Localizacion", blank=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.desclocalizacion
    
    class Meta:        
        db_table = 'PUNTO_LOCALIZACION'


class PuntoSignificado(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    descsignificado = RichTextField(db_column='DescSignificado', verbose_name="Significado", blank=True)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.descsignificado
    
    class Meta:        
        db_table = 'PUNTO_SIGNIFICADO'


class PuntoSintomatologia(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    nomorgpartecuerpo = models.ForeignKey(ParteCuerpo, models.DO_NOTHING)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)


    def __str__(self) -> str:
        return self.nomorgpartecuerpo
    
    class Meta:        
        db_table = 'PUNTO_SINTOMATOLOGIA'


class PuntoVideos(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    ligavideo = models.CharField(db_column='LigaVideo', max_length=255, blank=True)
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
    nombre = models.CharField( max_length=80)
    parte = models.ForeignKey(ParteCuerpo, models.CASCADE)
    tipo_punto = models.ForeignKey(TipoPunto, models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class PuntoEmocion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    emocion = models.ForeignKey(Emocion, models.CASCADE)

class Elementos(models.Model):
    nombre = models.CharField( max_length=30, default='')
    descripcion = models.CharField( max_length=240, default='')
    
    def __str__(self) -> str:
        return self.nombre

class PuntoElemento(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.CASCADE)
    elemento = models.ForeignKey(Elementos, models.CASCADE)


