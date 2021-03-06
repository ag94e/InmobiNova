from django.http import HttpResponse
from django.shortcuts import render, redirect
from gestionpedidos.models import houses
from django.core.mail import send_mail
from django.conf import settings
from gestionpedidos.forms import formContacto, crearUsuario, AgregarPropiedad
from django.contrib.auth import login as do_login, authenticate


def renderview(request):

    busqueda = houses.objects.all().order_by('created')

    return render(request, "base.html", {'casas': busqueda})


def register(request):

    data = {
        'form': crearUsuario
    }

    if request.method == 'POST':
        formulario = crearUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            do_login(request, user)
            return redirect(to='home')
        data["form"] = formulario

    return render(request, "reigster.html", data)


def houses_list(request):

    search_field = request.GET.get('search_field')

    if search_field:
        busqueda = houses.objects.filter(city__icontains=search_field).order_by('created').reverse()
    else:
        busqueda = houses.objects.all().order_by('created').reverse()

    formulario_test = AgregarPropiedad(request.POST)

    if request.method == 'POST':

        formulario_test = AgregarPropiedad(request.POST)

        if formulario_test.is_valid():
            ff = formulario_test.cleaned_data

            new_house = houses.objects.create(city=ff['ciudad'], description=ff['descripcion'], price=ff['precio'], image=ff['imagen'])
            new_house.save()

    return render(request, "houses.html", {'casas': busqueda, 'peticion': search_field, 'formulario': formulario_test})


def contact(request):

    if request.method == "POST":

        miform = formContacto(request.POST)

        if miform.is_valid():
            fullform = miform.cleaned_data

            send_mail(fullform['asunto'], fullform['mensaje'] + ' Remitente : ' + fullform['mail'], fullform.get('mail', 'brayanpotosimail@gmail.com'), ['brayanpotosidev@gmail.com'],)

            return HttpResponse("Enviado con exito")

    else:
        miform = formContacto()

    return render(request, 'contact.html', {'formi': miform})


def login(request):

    return render(request, "login.html")

