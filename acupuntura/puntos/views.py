from django.shortcuts import render
from django.shortcuts import  get_object_or_404, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse
from django.template import loader
from django.contrib import messages

import logging

# Create your views here.

from . import models as modelos

from . import forms as formularios


from .forms import (PuntoImagenesFormSet, PuntoCaracteristicasFormSet, \
                    PuntoDocumentosFormSet,  PuntoSignificadoFormSet, \
                    PuntoEnfermedadFormSet, PuntoImagenLocalizacionFormSet, \
                    PuntoLocalizacionFormSet, PuntoVideoFormSet\
                    )

class lista_canales(ListView):
    model = modelos.CanalAcupuntura
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
    model = modelos.CanalAcupuntura
    success_url = reverse_lazy('lista_canales')
    fields = ['cvecanal', 'nomcanal', 'trayecto','nomchino', 'traduccion', 'numtotalpuntos', 'bandactivo']
    template_name = 'catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Canal"
        context['regresa'] = 'lista_canales'
        return context

class update_canal(UpdateView):
    model = modelos.CanalAcupuntura
    fields = ['cvecanal', 'nomcanal', 'trayecto','nomchino', 'traduccion', 'numtotalpuntos', 'bandactivo']
    success_url = reverse_lazy('lista_canales')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Canal"
        context['regresa'] = 'lista_canales'
        return context
    
class detalle_canal(DetailView):
    model = modelos.CanalAcupuntura
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_canales')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Canal"
        context['regresa'] = 'lista_canales'
        return context   


class borra_canal(DeleteView):
    model = modelos.CanalAcupuntura
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
    model = modelos.PuntoAcupuntura
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
            'detalle':'update_punto',
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
    model = modelos.PuntoAcupuntura
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
    model = modelos.PuntoAcupuntura
    form_class = formularios.PuntoAcupunturaForm
    success_url = reverse_lazy('lista_puntos')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Punto"
        context['regresa'] = 'lista_puntos'
        return context
    
class detalle_punto(DetailView):
    model = modelos.PuntoAcupuntura
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_puntos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Canal"
        context['regresa'] = 'lista_puntos'
        return context   


class borra_punto(DeleteView):
    model = modelos.PuntoAcupuntura
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_puntos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Canal"
        context['regresa'] = 'lista_puntos'
        return context   
    
# Fomularios de puntos


class PuntoInline():
    form_class = formularios.PuntoAcupunturaForm
    model = modelos.PuntoAcupuntura
    template_name = "punto/punto.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, f'formset_{name}_valid', None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('lista_puntos')

    def formset_imagenes_valid(self, formset):
        for obj in formset.deleted_objects:
            obj.delete()
        for imagen in formset:
            if imagen.is_valid():
                imagen.cvepunto = self.object
                imagen.save()

    def formset_documentos_valid(self, formset):
        documentos = formset.save(commit=False)  
        for obj in formset.deleted_objects:
            obj.delete()
        for documento in formset:
            if documento.is_valid():
                documento.cvepunto = self.object
                documento.save()

    def formset_caracteristicas_valid(self, formset):
        for obj in formset.deleted_objects:
            obj.delete()
        for caracteristica in formset:
            if caracteristica.is_valid():
                caracteristica.cvepunto = self.object
                caracteristica.save()    
                        
    def formset_significados_valid(self, formset):
        for obj in formset.deleted_objects:
            obj.delete()
        for significado  in formset:
            if significado.is_valid():
                significado = significado.save(commit=False)
                significado.cvepunto = self.object
                significado.save()
                                
    def formset_enfermedades_valid(self, formset):
        for obj in formset.deleted_objects:
            obj.delete()
        for enfermedad in formset:
            if enfermedad.is_valid():
                enfermedad = enfermedad.save(commit=False)
                enfermedad.cvepunto = self.object
                enfermedad.save()

    def formset_imagen_localizaciones_valid(self, formset):
        for obj in formset.deleted_objects:
            obj.delete()
        for imagen_localizacion in formset:
            if imagen_localizacion.is_valid():
                imagen_localizacion = imagen_localizacion.save(commit=False)
                imagen_localizacion.cvepunto = self.object
                imagen_localizacion.save()
                    
                    
    def formset_localizaciones_valid(self, formset):
        for obj in formset.deleted_objects:
            obj.delete()
        for localizacion in formset:
            if localizacion.is_valid():
                localizacion = localizacion.save(commit=False)
                localizacion.cvepunto = self.object
                localizacion.save()

    def formset_videos_valid(self, formset):   
        for obj in formset.deleted_objects:
            obj.delete()
        for video in formset:
            if video.is_valid():
                video = video.save(commit=False)  
                video.cvepunto = self.object
                video.save()

class PuntoCreate(PuntoInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(PuntoCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'imagenes': PuntoImagenesFormSet(prefix='imagenes'),
                'documentos': PuntoDocumentosFormSet(prefix='documentos'),
                'caracteristicas': PuntoCaracteristicasFormSet(prefix='caracteristicas'),
                'significados': PuntoSignificadoFormSet(prefix='significados'),
                'enfermedades': PuntoEnfermedadFormSet(prefix='enfermedades'),
                'imagen_localizaciones': PuntoImagenLocalizacionFormSet(prefix='imagen_localizaciones'),
                'localizaciones': PuntoLocalizacionFormSet(prefix='localizaciones'),
                'videos': PuntoVideoFormSet(prefix='videos'),
            }
        else:
            return {
                'imagenes': PuntoImagenesFormSet(self.request.POST or None, self.request.FILES or None, prefix='imagenes'),
                'documentos': PuntoDocumentosFormSet(self.request.POST or None, self.request.FILES or None, prefix='documentos'),
                'caracteristicas': PuntoCaracteristicasFormSet(self.request.POST or None, self.request.FILES or None, prefix='caracteristicas'),
                'significados': PuntoSignificadoFormSet(self.request.POST or None, self.request.FILES or None, prefix='significados'),
                'enfermedades': PuntoEnfermedadFormSet(self.request.POST or None, self.request.FILES or None, prefix='enfermedades'),
                'imagen_localizaciones': PuntoImagenLocalizacionFormSet(self.request.POST or None, self.request.FILES or None, prefix='imagen_localizaciones'),
                'localizaciones': PuntoLocalizacionFormSet(self.request.POST or None, self.request.FILES or None, prefix='localizaciones'),
                'videos': PuntoVideoFormSet(self.request.POST or None, self.request.FILES or None, prefix='videos'),
            }


def PuntoUpdate2(request, pk):
    punto = get_object_or_404(modelos.PuntoAcupuntura, pk=pk)    
    form = formularios.PuntoAcupunturaForm(request.POST or None, request.FILES or None,  instance=punto)
    # Initialize the formset    
    imagenes =  formularios.PuntoImagenesFormSet(prefix='imagenes', instance=punto, data=request.POST or None, files=request.FILES or None),
    documentos =  formularios.PuntoDocumentosFormSet(prefix='documentos', instance=punto, data=request.POST or None, files=request.FILES or None),
    caracteristicas =  formularios.PuntoCaracteristicasFormSet(prefix='caracteristicas', instance=punto, data=request.POST or None, files=request.FILES or None),
    significados =  formularios.PuntoSignificadoFormSet(prefix='significados', instance=punto, data=request.POST or None, files=request.FILES or None),
    enfermedades =  formularios.PuntoEnfermedadFormSet(prefix='enfermedades', instance=punto, data=request.POST or None, files=request.FILES or None),
    imagen_localizaciones =  formularios.PuntoImagenLocalizacionFormSet(prefix='imagen_localizaciones', instance=punto, data=request.POST or None, files=request.FILES or None),
    localizaciones =  formularios.PuntoLocalizacionFormSet(prefix='localizaciones', instance=punto, data=request.POST or None, files=request.FILES or None),
    videos =  formularios.PuntoVideoFormSet(prefix='videos', instance=punto, data=request.POST or None, files=request.FILES or None),
    nombres = ('imagenes','documentos','caracteristicas','significados','enfermedades','imagen_localizaciones','localizaciones','videos') 
    if request.method == 'POST':
        print("Se empieza a procesar los formularios")
        if form.has_changed():
            print(f"El punto cambio: {punto}")
            if form.is_valid():
                print("El punto guardara")
                form.save()

        for nombre in nombres:
            try:
                for formm in eval(nombre):
                    if formm.is_valid():
                        print(f"Se guardara un form de {nombre}")
                        formm.cvepunto = punto
                        formm.save()
                        #messages.success(request, f"{nombre} -- se guardaron cambios.")
                    else:
                        print(request, f"{nombre} -- Please correct the errors below.")
                
            except Exception as e:
                print(f"fallo por: {e}")

        return redirect('update_punto2', pk=punto.pk)
    
    else:
        logging.info("Se empieza a procesar los formularios")
        # Render the template for GET and POST with errors
        return render(request, 'punto/punto2.html', {
            'imagenes':imagenes,
            'documentos':documentos,
            'caracteristicas':caracteristicas,
            'significados':significados,
            'enfermedades':enfermedades,
            'imagen_localizaciones':imagen_localizaciones,
            'localizaciones':localizaciones,
            'videos':videos,
            'punto': punto,
            'form' : form
        })


class PuntoUpdate(PuntoInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(PuntoUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'imagenes': PuntoImagenesFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='imagenes'),
            'documentos': PuntoDocumentosFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='documentos'),
            'caracteristicas': PuntoCaracteristicasFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='caracteristicas'),
            'significados': PuntoSignificadoFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='significados'),
            'enfermedades': PuntoEnfermedadFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='enfermedades'),
            'imagen_localizaciones': PuntoImagenLocalizacionFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='imagen_localizaciones'),
            'localizaciones': PuntoLocalizacionFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='localizaciones'),
            'videos': PuntoVideoFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='videos'),
        }
    
############ ENFERMEDADES ##############


class lista_enfermedades(ListView):
    model = modelos.Enfermedad
    template_name  = 'catalogos/listenfermedad.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Enfermedades",
            'add':"add_enfermedad",
            'add_label':'Nueva Enfermedad',
            'update':'update_enfermedad',  
            'detalle':'detalle_enfermedad',
            'borra':'borra_enfermedad',
            'encabezados': {"clave":"CLAVE","nombre":"NOMBRE", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context    
    

class add_enfermedad(CreateView):
    model = modelos.Enfermedad
    success_url = reverse_lazy('lista_enfermedades')
    fields = ['cveenfermedad', 'nomenfermedad','bandactivo']
    template_name = 'catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Enfermedad"
        context['regresa'] = 'lista_enfermedades'
        return context

class update_enfermedad(UpdateView):
    model = modelos.Enfermedad
    fields = ['cveenfermedad', 'nomenfermedad','bandactivo']
    success_url = reverse_lazy('lista_enfermedades')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Enfermedad"
        context['regresa'] = 'lista_enfermedades'
        return context
    
class detalle_enfermedad(DetailView):
    model = modelos.Enfermedad
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_enfermedades')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Enfermedad"
        context['regresa'] = 'lista_enfermedades'
        return context   


class borra_enfermedad(DeleteView):
    model = modelos.Enfermedad
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_enfermedades')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borra Enfermedad"
        context['regresa'] = 'lista_enfermedades'
        return context   