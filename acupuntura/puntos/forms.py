from django import forms
from django.forms import inlineformset_factory, BaseFormSet, formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML, Submit
from .models import (PuntoAcupuntura, PuntoCaracteristicas, PuntoDocumentos, 
                     PuntoEnfermedad, PuntoImagenes, PuntoImagenLocalizacion, 
                     PuntoLocalizacion, PuntoSignificado, PuntoVideos)

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('cvepunto',css_class='col-4'),
                Div('nompunto', css_class='col-4'),
                Div('cvecanal', css_class='col-4'),
                css_class='row'
            ),
            Div(
                Div('nomlargopunto',css_class='col-6'),
                Div('bandactivo', css_class='col-2'),
                Div(Submit('submit', 'Guardar', css_class='button white'), css_class='col-4'),
                css_class='row'
            ),
        )
        self.fields['bandactivo'].widget.attrs['class'] =  'form-check-input'

class PuntoCaracteristicasForm(forms.ModelForm):
    class Meta:
        model = PuntoCaracteristicas
        fields = ('desccaracteristicas', )

PuntoCaracteristicasFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoCaracteristicas, form=PuntoCaracteristicasForm,
    extra=1, min_num=1, max_num=1, can_delete=True, can_delete_extra=True
)

class PuntoDocumentosForm(forms.ModelForm):
    class Meta:
        model = PuntoDocumentos
        fields = ('ligadocumento', )

PuntoDocumentosFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoDocumentos, form=PuntoDocumentosForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoEnfermedadForm(forms.ModelForm):
    class Meta:
        model = PuntoEnfermedad
        fields = ('cveenfermedad', )

PuntoEnfermedadFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoEnfermedad, form=PuntoEnfermedadForm,
    extra=4, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoImagenesForm(forms.ModelForm):
    class Meta:
        model = PuntoImagenes
        fields = ('ligaimagen',)


PuntoImagenesFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoImagenes, form=PuntoImagenesForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoImagenLocalizacionForm(forms.ModelForm):
    class Meta:
        model = PuntoImagenLocalizacion
        fields = ('ligaimagen', )

PuntoImagenLocalizacionFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoImagenLocalizacion, form=PuntoImagenLocalizacionForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoLocalizacionForm(forms.ModelForm):
    class Meta:
        model = PuntoLocalizacion
        fields = ('desclocalizacion', )

PuntoLocalizacionFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoLocalizacion, form=PuntoLocalizacionForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoSignificadoForm(forms.ModelForm):
    class Meta:
        model = PuntoSignificado
        fields = ('descsignificado', )

PuntoSignificadoFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoSignificado, form=PuntoSignificadoForm,
    extra=1, min_num=1, max_num=1, can_delete=True, can_delete_extra=True
)

class PuntoVideoForm(forms.ModelForm):
    class Meta:
        model = PuntoVideos
        fields = ('ligavideo', )

PuntoVideoFormSet = inlineformset_factory(
    PuntoAcupuntura, PuntoVideos, form=PuntoVideoForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)


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