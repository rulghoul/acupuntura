from django import forms
from django.forms import inlineformset_factory, BaseFormSet, formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML, Submit

from . import models as modelos

from betterforms.multiform import MultiModelForm
from collections import OrderedDict

class PuntoAcupunturaForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoAcupuntura
        fields = ['cvepunto', 'nompunto', 'nomchino', 'cvecanal', 'bandactivo']
        labels = {
            'cvepunto': 'Clave del punto',
            'nompunto': 'Nombre del punto',
            'nomchino': 'Nombre Chino',
            'cvecanal': 'Canal de acupuntura',
            'bandactivo': 'Activo',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # No cerrar el tag del formulario
        self.helper.layout = Layout(
            Div(
                Div('cvepunto',css_class='col-4'),
                Div('nompunto', css_class='col-4'),
                Div('cvecanal', css_class='col-4'),
                css_class='row'
            ),
            Div(
                Div('nomchino',css_class='col-6'),
                Div('bandactivo', css_class='col-2'),
                Div(Submit('submit', 'Guardar', css_class='button white '), css_class='col-4'),
                css_class='row'
            ),
        )
        self.fields['bandactivo'].widget.attrs['class'] =  'form-check-input'

class PuntoCaracteristicasForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoCaracteristicas
        fields = ('desccaracteristicas', )

PuntoCaracteristicasFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoCaracteristicas, form=PuntoCaracteristicasForm,
    extra=1, min_num=1, max_num=1, can_delete=True, can_delete_extra=True
)

class PuntoDocumentosForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoDocumentos
        fields = ('ligadocumento', )

PuntoDocumentosFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoDocumentos, form=PuntoDocumentosForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoEnfermedadForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoEnfermedad
        fields = ('cveenfermedad', )

PuntoEnfermedadFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoEnfermedad, form=PuntoEnfermedadForm,
    extra=2, min_num=1, max_num=5, can_delete=True, can_delete_extra=True
)

class PuntoImagenesForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoImagenes
        fields = ('ligaimagen',)


PuntoImagenesFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoImagenes, form=PuntoImagenesForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoImagenLocalizacionForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoImagenLocalizacion
        fields = ('ligaimagen', )

PuntoImagenLocalizacionFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoImagenLocalizacion, form=PuntoImagenLocalizacionForm,
    extra=0, min_num=1, max_num=1, can_delete=True, can_delete_extra=True
)

class PuntoLocalizacionForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoLocalizacion
        fields = ('desclocalizacion', )

PuntoLocalizacionFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoLocalizacion, form=PuntoLocalizacionForm,
    extra=2, min_num=1, max_num=4, can_delete=True, can_delete_extra=True
)

class PuntoSignificadoForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoSignificado
        fields = ('descsignificado', )

PuntoSignificadoFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoSignificado, form=PuntoSignificadoForm,
    extra=1, min_num=1, max_num=1, can_delete=True, can_delete_extra=True
)

class PuntoSintomaForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoSintomatologia
        fields = ('sintoma', )

PuntoSintomaFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoSintomatologia, form=PuntoSintomaForm,
    extra=2, min_num=1, max_num=5, can_delete=True, can_delete_extra=True
)

class PuntoVideoForm(forms.ModelForm):
    class Meta:
        model = modelos.PuntoVideos
        fields = ('ligavideo', )

PuntoVideoFormSet = inlineformset_factory(
    modelos.PuntoAcupuntura, modelos.PuntoVideos, form=PuntoVideoForm,
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
    
# Emociones y Elementos

class EmocionesForm(forms.ModelForm):
    class Meta:
        model = modelos.CanalEmocion
        fields = ('emocion',)

EmocionesFormSet = inlineformset_factory(
    modelos.CanalAcupuntura, modelos.CanalEmocion, form=EmocionesForm,
    extra=1, min_num=1, max_num=3, can_delete=True, can_delete_extra=True
)


class ElementosForm(forms.ModelForm):
    class Meta:
        model = modelos.CanalElemento
        fields = ('elemento', )

ElementosFormSet = inlineformset_factory(
    modelos.CanalAcupuntura, modelos.CanalElemento, form=ElementosForm,
    extra=0, min_num=1, max_num=1, can_delete=True, can_delete_extra=True
)


class CanalAcupunturaForm(forms.ModelForm):
    class Meta:
        model = modelos.CanalAcupuntura
        fields = ['cvecanal', 'nomcanal', 'nomchino', 'bandactivo']
        labels = {
            'cvepunto': 'Clave del Canal',
            'nomcanal': 'Nombre del Canal',
            'nomchino': 'Nombre Chino',
            'bandactivo': 'Activo',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # No cerrar el tag del formulario
        self.helper.layout = Layout(
            Div(
                Div('cvecanal',css_class='col-4'),
                Div('nomcanal', css_class='col-4'),
                Div('nomchino', css_class='col-4'),
                css_class='row'
            ),
            Div(
                Div('bandactivo', css_class='col-2'),
                Div(Submit('submit', 'Guardar', css_class='button white '), css_class='col-4'),
                css_class='row'
            ),
        )
        self.fields['bandactivo'].widget.attrs['class'] =  'form-check-input'
