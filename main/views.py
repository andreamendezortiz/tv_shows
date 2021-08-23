from django.shortcuts import render, redirect, HttpResponse
from .models import Show, Network
from django.contrib import messages

def index(request):
    return redirect('/shows')


def shows(request):
    shows = Show.objects.all()
    networks = Network.objects.all()

    context = {
        'shows': shows,
        'networks': networks
    }

    return render(request, 'shows.html', context)


def new(request):
    networks = Network.objects.all()
    shows = Show.objects.all()

    context = {
        'networks': networks,
        'shows': shows
    }

    return render(request, 'new.html', context)


def create(request):

    shows_title = request.POST['title']
    shows_description = request.POST['description']
    shows_release_date = request.POST['release_date']
    network_id = int(request.POST['network'])

    Show.objects.create(title=shows_title, description=shows_description, release_date=shows_release_date, network_id=network_id)

    messages.success(request, f'El programa {shows_title} ha sido agregado')
    

    return redirect('/shows')



def id(request, id):
    networks = Network.objects.all()
    shows = Show.objects.all()
    selec_show = Show.objects.get(id=id)

    context = {
        'networks': networks,
        'shows': shows,
        'selec_show': selec_show
    }
    
    return render(request, 'id.html', context)


def update(request, id):
    networks = Network.objects.all()
    show = Show.objects.get(id=id)

    context = {
        'networks': networks,
        'show': show,
    }

    return render(request, 'update.html', context)


def edit(request, id):

    # nos traemos el show a cambiar
    show = Show.objects.get(id=id)

    show.title = request.POST['title']
    show.description = request.POST['description']
    show.network_id = int(request.POST['network'])
    show.release_date = request.POST['release_date']
    

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for key, value in errors.items():
            messages.error(request, value)
        # redirigir al usuario al formulario para corregir los errores
        return redirect(f'/shows/{id}/update')
    show.save()
    messages.success(request, f'El programa {show.title} fue actualizado con éxito')
    return redirect("/shows")







def destroy(request):
    context = {
    'saludo': 'Hola'
    }
    
    return render(request, 'shows.html', context)
