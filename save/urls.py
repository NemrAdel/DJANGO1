from django.urls import path
from . import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('TicketFootball/',views.ticketfootball,name='ticketfootball'),
    path('TicketCinema/',views.ticketcinema,name='ticketcinema'),
    path('TicketPlane/',views.ticketplane,name='ticketplane'),
]