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
            'detalle':'detalle_punto',
            'borra':'borra_punto',
            'encabezados': {"clave":"CLAVE",
                            "nombre":"NOMBRE", 
                            "largo":"NOMBRE CHINO",
                            "canal":"CANAL",
                            "activo":"ACTIVO"
                            },
        }
        context.update(datos)
        return context    
    
class add_punto(CreateView):
    model = modelos.PuntoAcupuntura
    success_url = reverse_lazy('update_punto')
    fields = ['cvepunto', 'nompunto', 'nomchino', 'cvecanal', 'bandactivo']
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
    template_name = 'punto/detalle.html'
    success_url = reverse_lazy('lista_puntos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Punto"
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
        
def PuntoForm(request, pk, titulo):
    if pk:
        punto = get_object_or_404(modelos.PuntoAcupuntura, pk=pk)    
    else:
        punto = modelos.PuntoAcupuntura()   
    form = formularios.PuntoAcupunturaForm(request.POST or None, request.FILES or None,  instance=punto)
    # Initialize the formset    
    imagenes =  formularios.PuntoImagenesFormSet(prefix='imagenes', instance=punto, data=request.POST or None, files=request.FILES or None)
    documentos =  formularios.PuntoDocumentosFormSet(prefix='documentos', instance=punto, data=request.POST or None, files=request.FILES or None)
    caracteristicas =  formularios.PuntoCaracteristicasFormSet(prefix='caracteristicas', instance=punto, data=request.POST or None, files=request.FILES or None)
    significados =  formularios.PuntoSignificadoFormSet(prefix='significados', instance=punto, data=request.POST or None, files=request.FILES or None)
    enfermedades =  formularios.PuntoEnfermedadFormSet(prefix='enfermedades', instance=punto, data=request.POST or None, files=request.FILES or None)
    imagen_localizaciones =  formularios.PuntoImagenLocalizacionFormSet(prefix='imagen_localizaciones', instance=punto, data=request.POST or None, files=request.FILES or None)
    localizaciones =  formularios.PuntoLocalizacionFormSet(prefix='localizaciones', instance=punto, data=request.POST or None, files=request.FILES or None)
    sintomas =  formularios.PuntoSintomaFormSet(prefix='sintomas', instance=punto, data=request.POST or None, files=request.FILES or None)
    videos =  formularios.PuntoVideoFormSet(prefix='videos', instance=punto, data=request.POST or None, files=request.FILES or None)
    nombres = ('imagenes','documentos','caracteristicas','significados','enfermedades','imagen_localizaciones','localizaciones','videos', 'elementos', 'emociones', 'sintomas') 
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
                        formm.save()
                        #messages.success(request, f"{nombre} -- se guardaron cambios.")
                    else:
                        #messages.warning(request, f"{nombre} -- Please correct the errors below.")
                        #print( f"{nombre} {formm.errors}")
                        pass
                
            except Exception as e:
                #messages.warning(request,f"fallo por: {e}")
                #print(f"fallo por: {e}")
                pass

        return redirect('update_punto', pk=punto.pk)
    
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
            'sintomas': sintomas,
            'punto': punto,
            'form' : form,
            'titulo': titulo
        })


def PuntoUpdate(request, pk):
    return PuntoForm(request, pk, "Actualiza Punto")

def PuntoAdd(request):
    return PuntoForm(request, None, "Nuevo Punto")
    
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
    

# Emociones y Elementos

class lista_emociones(ListView):
    model = modelos.Emocion
    template_name  = 'catalogos/lista_emocion.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Emociones",
            'add':"add_emocion",
            'add_label':'Nueva Emocion',
            'update':'update_emocion',  
            'detalle':'detalle_emocion',
            'borra':'borra_emocion',
            'encabezados': {"nombre":"NOMBRE","parte":"PARTE DEL CUERPO", "tipo_punto":"TIPO DE PUNTO"},
        }
        context.update(datos)
        return context    

class add_emocion(CreateView):
    model = modelos.Emocion
    success_url = reverse_lazy('lista_emociones')
    fields = ['nombre', ]
    template_name = 'catalogos/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Emocion"
        context['regresa'] = 'lista_emociones'
        return context


class update_emocion(UpdateView):
    model = modelos.Emocion
    fields = ['nombre', ]
    success_url = reverse_lazy('lista_emociones')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Emocion"
        context['regresa'] = 'lista_emociones'
        return context
    
   
class detalle_emocion(DetailView):
    model = modelos.Emocion
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_emociones')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Emocion"
        context['regresa'] = 'lista_emociones'
        return context   


class borra_emocion(DeleteView):
    model = modelos.Emocion
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_emociones')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Emocion"
        context['regresa'] = 'lista_emociones'
        return context   
    


# Parte de Cuerpo

class lista_partes(ListView):
    model = modelos.ParteCuerpo
    template_name  = 'catalogos/list_parte.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Partes del cuerpo",
            'add':"add_parte",
            'add_label':'Nueva parte del cuerpo',
            'update':'update_parte',  
            'detalle':'detalle_parte',
            'borra':'borra_parte',
            'encabezados': {"nombre":"NOMBRE","parte":"PARTE DEL CUERPO", "tipo_punto":"TIPO DE PUNTO"},
        }
        context.update(datos)
        return context    

class add_parte(CreateView):
    model = modelos.ParteCuerpo
    success_url = reverse_lazy('lista_partes')
    fields = ['nombre', ]
    template_name = 'catalogos/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva parte del cuerpo"
        context['regresa'] = 'lista_partes'
        return context


class update_parte(UpdateView):
    model = modelos.ParteCuerpo
    fields = ['nombre', ]
    success_url = reverse_lazy('lista_partes')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza parte del cuerpo"
        context['regresa'] = 'lista_partes'
        return context
    
   
class detalle_parte(DetailView):
    model = modelos.ParteCuerpo
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_partes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle parte del cuerpo"
        context['regresa'] = 'lista_partes'
        return context   


class borra_parte(DeleteView):
    model = modelos.ParteCuerpo
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_partes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar parte del cuerpo"
        context['regresa'] = 'lista_partes'
        return context   


# Elementos


class lista_elementos(ListView):
    model = modelos.Elementos
    template_name  = 'catalogos/lista_elementos.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Elementos",
            'add':"add_elemento",
            'add_label':'Nuevo Elemento',
            'update':'update_elemento',  
            'detalle':'detalle_elemento',
            'borra':'borra_elemento',
            'encabezados': {"nombre":"NOMBRE", "descripcion":"DESCRIPCION"},
        }
        context.update(datos)
        return context    

class add_elemento(CreateView):
    model = modelos.Elementos
    success_url = reverse_lazy('lista_elementos')
    fields = ['nombre', 'descripcion']
    template_name = 'catalogos/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Elemento"
        context['regresa'] = 'lista_elementos'
        return context


class update_elemento(UpdateView):
    model = modelos.Elementos
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('lista_elementos')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Elemento"
        context['regresa'] = 'lista_elementos'
        return context
    
   
class detalle_elemento(DetailView):
    model = modelos.Elementos
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_elementos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Elemento"
        context['regresa'] = 'lista_elementos'
        context['datos'] = modelos.TipoPunto.objects.all()
        return context   


class borra_elemento(DeleteView):
    model = modelos.Elementos
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_elementos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Elemento"
        context['regresa'] = 'lista_elementos'
        return context   
    


def CanalForm(request, pk, titulo):
    if pk:
        canal = get_object_or_404(modelos.CanalAcupuntura, pk=pk)    
    else:
        canal = modelos.CanalAcupuntura()
    form = formularios.CanalAcupunturaForm(request.POST or None, request.FILES or None,  instance=canal)
    # Initialize the formset    
    emociones =  formularios.EmocionesFormSet(prefix='emociones', instance=canal, data=request.POST or None, files=request.FILES or None)
    elementos =  formularios.ElementosFormSet(prefix='elementos', instance=canal, data=request.POST or None, files=request.FILES or None)

    nombres = ('emociones','elementos') 
    if request.method == 'POST':
        print("Se empieza a procesar los formularios")
        if form.has_changed():
            canal.set
            if form.is_valid():
                print("El canal guardara")
                form.save()

        for nombre in nombres:
            try:
                for formm in eval(nombre):
                    if formm.is_valid():
                        print(f"Se guardara un form de {nombre}")
                        formm.save()
                        #messages.success(request, f"{nombre} -- se guardaron cambios.")
                    else:
                        #messages.warning(request, f"{nombre} -- Please correct the errors below.")
                        #print( f"{nombre} {formm.errors}")
                        pass
                
            except Exception as e:
                #messages.warning(request,f"fallo por: {e}")
                #print(f"fallo por: {e}")
                pass

        return redirect('update_canal', pk=canal.pk)
    
    else:
        logging.info("Se empieza a procesar los formularios")
        # Render the template for GET and POST with errors
        return render(request, 'punto/canal.html', {
            'emociones':emociones,
            'elementos':elementos,
            'form' : form,
            'titulo': titulo
        })


def UpdateCanalForm(request, pk):
    return CanalForm(request, pk, "Actualiza Canal")

def AddCanalForm(request):
    return CanalForm(request, None, "Nuevo Canal")



# Sintomas

class lista_sintomas(ListView):
    model = modelos.Sintoma
    template_name  = 'catalogos/list_sintomas.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Sintomas",
            'add':"add_sintoma",
            'add_label':'Nuevo Sintoma',
            'update':'update_sintoma',  
            'detalle':'detalle_sintoma',
            'borra':'borra_sintoma',
            'encabezados': {"sintoma":"SINTOMA"},
        }
        context.update(datos)
        return context    

class add_sintoma(CreateView):
    model = modelos.Sintoma
    success_url = reverse_lazy('lista_sintomas')
    fields = ['sintoma', 'bandactivo']
    template_name = 'catalogos/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Sintoma"
        context['regresa'] = 'lista_sintomas'
        return context


class update_sintoma(UpdateView):
    model = modelos.Sintoma
    fields = ['sintoma', 'bandactivo']
    success_url = reverse_lazy('lista_sintomas')
    template_name = 'catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Sintoma"
        context['regresa'] = 'lista_sintomas'
        return context
    
   
class detalle_sintoma(DetailView):
    model = modelos.Sintoma
    template_name = 'catalogos/detalle.html'
    success_url = reverse_lazy('lista_sintomas')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Sintoma"
        context['regresa'] = 'lista_sintomas'
        return context   


class borra_sintoma(DeleteView):
    model = modelos.ParteCuerpo
    template_name = 'catalogos/borrar.html'
    success_url = reverse_lazy('lista_partes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar parte del cuerpo"
        context['regresa'] = 'lista_partes'
        return context   
