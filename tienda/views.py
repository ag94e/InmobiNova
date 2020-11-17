from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from gestionpedidos.models import usuarios, houses
from django.core.mail import send_mail
from django.conf import settings
from gestionpedidos.forms import formContacto, crearUsuario
from django.contrib.auth import login as do_login, authenticate

class persona(object):

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name


p1 = persona("nuevo", "usuario")


def fecha_hora(request):
    fecha = datetime.datetime.now()

    return HttpResponse(fecha)


def calcular_edad(request, year, edad):
    present_year = 2020
    edad_futura = edad + (year - present_year)

    resultado = f'tu edad para el año {year} sera {edad_futura}'

    return HttpResponse(resultado)


# def template_one(request):                         VISTA CREADA SIN CLASE LOADER
#
#     mi_lista = ["ziro", "one", "two"]
#
#     fecha = datetime.datetime.now()
#     name = "Pepito"
#     doc = open('C:/Users/X/Desktop/django/news2/news2/templates2/base.html')
#
#     doc_read = Template(doc.read())
#     doc.close()
#     ctx = Context({"first_name": p1.name, "ahoraes": fecha, "temas": mi_lista})
#
#     documento = doc_read.render(ctx)
#
#     return HttpResponse(documento)


#                                                      VISTA CREADA CON CLASE LOADER


def newvista(request):

    mi_lista = ["ziro", "one", "two"]

    fecha = datetime.datetime.now()

    doc = loader.get_template('base.html')
    resultado = doc.render({"first_name": p1.name, "ahoraes": fecha, "temas": mi_lista})

    return HttpResponse(resultado)


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

    return render(request, "houses.html", {'casas': busqueda, 'peticion': search_field})


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





    #     asunto = request.POST['asunto']
    #     message = request.POST['mansaje'] + ' /n/n de ' + request.POST['mail']
    #     mfrom = settings.EMAIL_HOST_USER
    #     recipient = ['brayanpotosidev@gmail.com']
    #
    #     send_mail(asunto, message, mfrom, recipient)
    #
    #     return HttpResponse("Enviado con exito")
    #
    # return render(request, "contact.html")


def login(request):

    return render(request, "login.html")

def test(request):

    return render(request, 'test.html')