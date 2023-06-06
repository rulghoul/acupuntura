from django import forms
from django.forms import inlineformset_factory, BaseFormSet, formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML
from .models import PuntoAcupuntura, PuntoCaracteristicas, PuntoDocumentos, PuntoEnfermedad, PuntoImagenes, PuntoImagenLocalizacion, PuntoLocalizacion, PuntoSignificado

from betterforms.multiform import MultiModelForm
from collections import OrderedDict

class PuntoAcupunturaForm(forms.ModelForm):
    class Meta:
        model = PuntoAcupuntura
        fields = ['cvepunto', 'nompunto', 'nomlargopunto', 'cvecanal', 'bandactivo']
        labels = {
            'cvepunto': 'Clave del punto',
            'nompunto': 'Nombre del punto',
            'nomlargopunto': 'Nombre largo del punto',
            'cvecanal': 'Canal de acupuntura',
            'bandactivo': 'Activo',
        }

class PuntoCaracteristicasForm(forms.ModelForm):
    class Meta:
        model = PuntoCaracteristicas
        fields = ('desccaracteristicas', )
    
class PuntoCaracteristicasFormSet(BaseFormSet):
    min_num=1
    max_num=4
    extra=2
    renderer=True
    form = formset_factory(PuntoCaracteristicasForm)
    use_required_attribute = True
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        kwargs['instance'] = self.instance
        return super()._construct_form(i, **kwargs)

class PuntoDocumentosForm(forms.ModelForm):
    class Meta:
        model = PuntoDocumentos
        fields = ('ligadocumento', )

class PuntoEnfermedadForm(forms.ModelForm):
    class Meta:
        model = PuntoEnfermedad
        fields = ('cveenfermedad', )

class PuntoImagenesForm(forms.ModelForm):
    class Meta:
        model = PuntoImagenes
        fields = ('ligaimagen', )

class PuntoImagenLocalizacionForm(forms.ModelForm):
    class Meta:
        model = PuntoImagenLocalizacion
        fields = ('ligaimagen', )

class PuntoLocalizacionForm(forms.ModelForm):
    class Meta:
        model = PuntoLocalizacion
        fields = ('desclocalizacion', )

class PuntoSignificadoForm(forms.ModelForm):
    class Meta:
        model = PuntoSignificado
        fields = ('descsignificado', )



class PuntoMultiForm(MultiModelForm):
    form_classes = OrderedDict((
        ('punto_acupuntura', PuntoAcupunturaForm),
        ('punto_caracteristicas', PuntoCaracteristicasForm),
        ('punto_documentos', PuntoDocumentosForm),
        ('punto_enfermedad', PuntoEnfermedadForm),
        ('punto_imagenes', PuntoImagenesForm),
        ('punto_imagen_localizacion', PuntoImagenLocalizacionForm),
        ('punto_localizacion', PuntoLocalizacionForm),
        ('punto_significado', PuntoSignificadoForm),
    ))

    def save(self, commit=True):
        objects = super(PuntoMultiForm, self).save(commit=False)

        if commit:
            punto = objects['punto_acupuntura']
            punto.save()
            caracteristica = self.forms['punto_caracteristicas']
            caracteristica.cvepunto = punto
            caracteristica.save()
            significado = objects['punto_significado']
            significado.cvepunto = punto
            significado.save()
            documento = objects['punto_documentos']
            documento.cvepunto = punto
            documento.save()
            enfermedad = objects['punto_enfermedad']
            enfermedad.cvepunto = punto
            enfermedad.save()
            imagen = objects['punto_imagenes']
            imagen.cvepunto = punto
            imagen.save()
            imagen_localizacion = objects['punto_imagen_localizacion']
            imagen_localizacion.cvepunto = punto
            imagen_localizacion.save()
            localizacion = objects['punto_localizacion']
            localizacion.cvepunto = punto
            localizacion.save()

        return objects