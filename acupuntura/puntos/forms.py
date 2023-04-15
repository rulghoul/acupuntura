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
        widgets = {
            'cvepunto': forms.TextInput(attrs={'class': 'form-control'}),
            'nompunto': forms.TextInput(attrs={'class': 'form-control'}),
            'nomlargopunto': forms.TextInput(attrs={'class': 'form-control'}),
            'cvecanal': forms.Select(attrs={'class': 'form-control'}),
            'bandactivo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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



class PuntoAcupunturaNestedForm(forms.Form):
    punto_acupuntura = PuntoAcupunturaForm(prefix='punto_acupuntura')
    punto_caracteristicas = PuntoCaracteristicasForm(prefix='punto_caracteristicas')
    punto_documentos = PuntoDocumentosForm(prefix='punto_documentos')
    # y así sucesivamente para cada modelo
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_method = 'post'
        helper.layout = Layout(
            Div(
                Fieldset('Punto de acupuntura',
                    Div(
                        'punto_acupuntura',
                        css_class='row',
                    ),
                ),
                Fieldset('Características',
                    Div(
                        'punto_caracteristicas',
                        css_class='row',
                    ),
                ),
                Fieldset('Documentos',
                    Div(
                        'punto_documentos',
                        css_class='row',
                    ),
                )
                # y así sucesivamente para cada modelo
            )
        )