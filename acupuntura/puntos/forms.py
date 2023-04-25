from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML
from .models import PuntoAcupuntura, PuntoCaracteristicas, PuntoDocumentos, PuntoEnfermedad, PuntoImagenes, PuntoImagenLocalizacion, PuntoLocalizacion, PuntoSignificado

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
        fields = ('desccaracteristicas', 'bandactivo')

class PuntoDocumentosForm(forms.ModelForm):
    class Meta:
        model = PuntoDocumentos
        fields = ('ligadocumento', 'bandactivo')

class PuntoEnfermedadForm(forms.ModelForm):
    class Meta:
        model = PuntoEnfermedad
        fields = ('cveenfermedad', 'bandactivo')

class PuntoImagenesForm(forms.ModelForm):
    class Meta:
        model = PuntoImagenes
        fields = ('ligaimagen', 'bandactivo')

class PuntoImagenLocalizacionForm(forms.ModelForm):
    class Meta:
        model = PuntoImagenLocalizacion
        fields = ('ligaimagen', 'bandactivo')

class PuntoLocalizacionForm(forms.ModelForm):
    class Meta:
        model = PuntoLocalizacion
        fields = ('desclocalizacion', 'bandactivo')

class PuntoSignificadoForm(forms.ModelForm):
    class Meta:
        model = PuntoSignificado
        fields = ('descsignificado', 'bandactivo')


