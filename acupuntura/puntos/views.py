from django.shortcuts import render
from django.shortcuts import  get_object_or_404, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse
from django.template import loader

# Create your views here.

from .models import (CanalAcupuntura, PuntoAcupuntura, \
                     PuntoCaracteristicas, PuntoDocumentos, \
                     PuntoEnfermedad, PuntoImagenes, \
                     PuntoImagenLocalizacion, PuntoLocalizacion, \
                     PuntoSignificado, PuntoSintomatologia, \
                     PuntoVideos,
                     )
from .forms import (PuntoImagenesForm, PuntoCaracteristicasForm, \
                    PuntoAcupunturaForm, PuntoDocumentosForm, \
                    PuntoEnfermedadForm, PuntoImagenLocalizacionForm, \
                    PuntoLocalizacionForm, PuntoSignificadoForm, \
                    PuntoMultiForm)

class lista_canales(ListView):
    model = CanalAcupuntura
    template_name  = 'catalogos/listcanal.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Canales",
            'add':"add_canal",
            'add_label':'Nuevo Canal',
            'update':'update_canal',  
            'detalle':'detalle_canal',
            'borra':'borra_canal',
            'encabezados': {"clave":"CLAVE","nombre":"NOMBRE", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context    
    

class add_canal(CreateView):
    model = CanalAcupuntura
    success_url = reverse_lazy('lista_canales')
    fields = ['cvecanal', 'nomcanal', 'bandactivo']
    template_name = 'catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Canal"
        context['regresa'] = 'lista_canales'
        return context

class update_canal(UpdateView):
    model = CanalAcupuntura
    fields = ['cvecanal', 'nomcanal', 'bandactivo']
    success_url = reverse_lazy('lista_canales')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Canal"
        context['regresa'] = 'lista_canales'
        return context
    
class detalle_canal(DetailView):
    model = CanalAcupuntura
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_canales')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Canal"
        context['regresa'] = 'lista_canales'
        return context   


class borra_canal(DeleteView):
    model = CanalAcupuntura
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_canales')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Canal"
        context['regresa'] = 'lista_canales'
        return context   

########### Puntos #############

class lista_puntos(ListView):
    model = PuntoAcupuntura
    template_name  = 'catalogos/listpuntos.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Puntos",
            'add':"add_punto",
            'add_label':'Nuevo Punto',
            'update':'update_punto',  
            'detalle':'update_punto2',
            'borra':'borra_punto',
            'encabezados': {"clave":"CLAVE",
                            "nombre":"NOMBRE", 
                            "largo":"NOMBRE LARGO",
                            "canal":"CANAL",
                            "activo":"ACTIVO"
                            },
        }
        context.update(datos)
        return context    
    
class add_punto(CreateView):
    model = PuntoAcupuntura
    success_url = reverse_lazy('update_punto')
    fields = ['cvepunto', 'nompunto', 'nomlargopunto', 'cvecanal', 'bandactivo']
    template_name = 'catalogos/add.html'
        
    def get_success_url(self):
        return reverse_lazy('update_punto', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Punto"
        context['regresa'] = 'lista_puntos'
        return context

class update_punto(UpdateView):
    model = PuntoAcupuntura
    form_class = PuntoAcupunturaForm
    success_url = reverse_lazy('lista_puntos')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Punto"
        context['regresa'] = 'lista_puntos'
        return context
    
class detalle_punto(DetailView):
    model = PuntoAcupuntura
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_puntos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Canal"
        context['regresa'] = 'lista_puntos'
        return context   


class borra_punto(DeleteView):
    model = PuntoAcupuntura
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_puntos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Canal"
        context['regresa'] = 'lista_puntos'
        return context   
    
# Fomularios de puntos


def actualiza_punto(request, pk):
    template = loader.get_template('actualiza_punto.html')
    punto = get_object_or_404(PuntoAcupuntura, pk=pk)
    #instancias de los detalles 

    print(punto.cvecanal, punto.cvepunto, punto.nomlargopunto)
    significado = punto.puntosignificado_set.first()
    imagen = punto.puntoimagenes_set.first()
    documento = punto.puntodocumentos_set.first()
    locali = punto.puntolocalizacion_set.first()
    enfermedad = punto.puntoenfermedad_set.first()
    caracteristica = punto.puntocaracteristicas_set.first()

    print(significado, documento, imagen, locali, enfermedad, caracteristica)
    if request.method == 'GET':
        form1 = PuntoAcupunturaForm(instance=punto)
        if form1.is_valid():
            form1.save()
        form2 = PuntoSignificadoForm(instance=significado)
        if form2.is_valid():
            form2.save()          
        form3 = PuntoImagenesForm(instance=imagen)
        if form3.is_valid():
            form3.save()
        form4 = PuntoDocumentosForm(instance=documento)
        if form4.is_valid():
            form4.save()
        form5 = PuntoImagenLocalizacionForm(instance=locali)
        if form5.is_valid():
            form5.save()
        form6 = PuntoEnfermedadForm(instance=enfermedad)
        if form6.is_valid():
            form6.save()
        form7 = PuntoCaracteristicasForm(instance=caracteristica)
        if form7.is_valid():
            form7.save()
            
    else:        
        form1 = PuntoAcupunturaForm(request.POST, instance=punto)
        form2 = PuntoSignificadoForm(request.POST, instance=significado)
        form3 = PuntoImagenesForm(request.POST, instance=imagen)
        form4 = PuntoDocumentosForm(request.POST, instance=documento)
        form5 = PuntoImagenLocalizacionForm(request.POST, instance=locali)
        form6 = PuntoEnfermedadForm(request.POST, instance=enfermedad)
        form7 = PuntoCaracteristicasForm(request.POST, instance=caracteristica)

        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
        if form3.is_valid():
            form3.save()
        if form4.is_valid():
            form4.save()
        if form5.is_valid():
            form5.save()
        if form6.is_valid():
            form6.save()
        if form7.is_valid():
            form7.save()
    
    

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
        'form6': form6,
        'form7': form7,
        'titulo': "Actualiza Punto"
    }

    return HttpResponse(template.render(context, request))

class punto_update2(UpdateView):
    model = PuntoAcupuntura
    form_class = PuntoMultiForm
    success_url = reverse_lazy('lista_puntos')
    template_name = 'catalogos/update2.html'

    def get_form_kwargs(self):
        kwargs = super(punto_update2, self).get_form_kwargs()
        punto =self.object
        kwargs.update(instance={
            'punto_acupuntura': self.object,
            'punto_caracteristicas': self.object.puntocaracteristicas_set.first(),
            'punto_significado' : punto.puntosignificado_set.first(),
            'punto_imagenes' : punto.puntoimagenes_set.first(),
            'punto_documentos' : punto.puntodocumentos_set.first(),
            'punto_localizacion' : punto.puntolocalizacion_set.first(),
            'punto_enfermedad' : punto.puntoenfermedad_set.first(),
            'punto_caracteristicas' : punto.puntocaracteristicas_set.first(),            
            'punto_imagen_localizacion': punto.puntoimagenlocalizacion_set.first(),
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        punto = self.object

        # Crear instancias de los formularios relacionados
        context['form_punto_caracteristicas'] = PuntoCaracteristicasForm(instance=punto.puntocaracteristicas_set.first())
        context['form_punto_significado'] = PuntoSignificadoForm(instance=punto.puntosignificado_set.first())
        context['form_punto_imagenes'] = PuntoImagenesForm(instance=punto.puntoimagenes_set.first())
        # Agregar más formularios relacionados aquí

        return context
    