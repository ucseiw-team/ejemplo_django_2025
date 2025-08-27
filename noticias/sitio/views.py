from datetime import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse

from sitio.models import Noticia
from sitio.forms import ContactForm


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.filter(archivada=False)

    return render(request, 'inicio.html', {'lista_noticias': noticias})


def ejemplo_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nueva = Noticia()
            nueva.titulo = 'nuevo contacto'
            nueva.texto = f"Nombre: {form.cleaned_data['nombre']}\n" \
                          f"Email: {form.cleaned_data['email']}\n" \
                          f"Mensaje: {form.cleaned_data['mensaje']}\n" \
                          f"Quiero recibir respuestas: {'Sí' if form.cleaned_data['quiero_recibir_respuestas'] else 'No'}"
            nueva.fecha = datetime.now()
            nueva.save()

            return redirect('inicio')
    else:
        form = ContactForm()

    return render(request, 'ejemplo_form.html', {'form': form})


def pedacito_noticias(request):
    noticias = Noticia.objects.filter(archivada=False).order_by('-fecha')[:5]
    return render(request, 'pedacito_noticias.html', {'lista_noticias': noticias})


def pedacito_noticias_json(request):
    noticias = Noticia.objects.filter(archivada=False).order_by('-fecha')[:5]
    respuesta = []
    for noticia in noticias:
        respuesta.append({
            'titulo': noticia.titulo,
            'texto': noticia.texto,
            'fecha': str(noticia.fecha),
        })
    return JsonResponse({"noticias": respuesta}, safe=False)
