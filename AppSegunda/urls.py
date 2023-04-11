from django.urls import path
from AppSegunda import views

urlpatterns = [
    path ("reserva", views.ReservaView, name='Reserva'),
    path ('reservaFormulario', views.ReservaFormulario, name="reservaFormulario"),
    
]