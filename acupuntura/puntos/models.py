from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.utils import timezone


class CanalAcupuntura(models.Model):
    cvecanal = models.CharField(db_column='CveCanal', max_length=20)
    nomcanal = models.CharField(db_column='NomCanal', max_length=80)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.nomcanal

    class Meta:        
        db_table = 'CANAL_ACUPUNTURA'


class Enfermedad(models.Model):
    cveenfermedad = models.CharField(db_column='CveEnfermedad', max_length=20)
    nomenfermedad = models.CharField(db_column='NomEnfermedad', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'ENFERMEDAD'

class Sintoma(models.Model):
    sintoma = models.CharField(db_column='Sintoma', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'SINTOMA'


class OrganoParteCuerpo(models.Model):
    nomorgpartecuerpo = models.CharField(db_column='NomOrgparteCuerpo', max_length=255)
    sintoma = models.ForeignKey(Sintoma, models.DO_NOTHING)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'ORGANO_PARTE_CUERPO'


class PuntoAcupuntura(models.Model):
    cvepunto =  models.CharField(db_column='CvePunto', max_length=20)  
    nompunto = models.CharField(db_column='NomPunto', max_length=80)
    nomlargopunto = models.CharField(db_column='NomLargoPunto', max_length=300)
    cvecanal = models.ForeignKey(CanalAcupuntura, models.DO_NOTHING)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    def __str__(self) -> str:
        return self.nompunto
    
    class Meta:        
        db_table = 'PUNTO_ACUPUNTURA'


class PuntoCaracteristicas(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    desccaracteristicas = RichTextField(db_column='DescCaracteristicas')
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_CARACTERISTICAS'


class PuntoDocumentos(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)     
    ligadocumento = models.CharField(db_column='LigaDocumento', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_DOCUMENTOS'


class PuntoEnfermedad(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)    
    cveenfermedad = models.ForeignKey(Enfermedad, models.DO_NOTHING)    
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_ENFERMEDAD'


class PuntoImagenes(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    ligaimagen = models.CharField(db_column='LigaImagen', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_IMAGENES'


class PuntoImagenLocalizacion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    ligaimagen = models.CharField(db_column='LigaImagen', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_IMAGEN_LOCALIZACION'


class PuntoLocalizacion(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    desclocalizacion = models.TextField(db_column='DescLocalizacion')
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_LOCALIZACION'


class PuntoSignificado(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    descsignificado = RichTextField(db_column='DescSignificado')
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_SIGNIFICADO'


class PuntoSintomatologia(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    nomorgpartecuerpo = models.ForeignKey(OrganoParteCuerpo, models.DO_NOTHING)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_SINTOMATOLOGIA'


class PuntoVideos(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    ligavideo = models.CharField(db_column='LigaVideo', max_length=255)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'PUNTO_VIDEOS'



class Sintomatologia(models.Model):
    cvepunto = models.ForeignKey(PuntoAcupuntura, models.DO_NOTHING)
    nomorgpartecuerpo = models.ForeignKey(OrganoParteCuerpo, models.DO_NOTHING)
    sintoma = models.ForeignKey(Sintoma, models.DO_NOTHING)
    bandactivo = models.BooleanField(db_column='BandActivo', default=True)
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate',default=timezone.now)

    class Meta:        
        db_table = 'SINTOMATOLOGIA'

