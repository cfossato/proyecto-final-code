from django.shortcuts import render
from AppSegunda.models import reserva #Avatar
from django.http import HttpResponse
#from AppSegunda.forms import  AvatarFormulario
from AppSegunda.forms import reservaFormulario

# Create your views here.
def ReservaView (request):
    return render(request,"reserva.html")

def ReservaFormulario(request):  
   if request.method == "POST": 
      miFormulario = reservaFormulario(request.POST, request.FILES)
      print(miFormulario.is_valid())
      print(miFormulario)

      if miFormulario.is_valid():   
         informacion = miFormulario.cleaned_data
         Reserva = reserva(nombre=informacion['nombre'], fechaDeEntrada=informacion['fechaDeEntrada'], pagado=informacion['pagado'], imagenreserva=informacion['imagenreserva']) 
         Reserva.save() 
         return render(request,"reservaFormulario.html",{"mensaje":"reserva creada con exito"})
 
      
      else: 
         miFormulario= reservaFormulario()
   else:
      miFormulario= reservaFormulario()
   return render(request,"reservaFormulario.html", {"miFormulario":miFormulario})
