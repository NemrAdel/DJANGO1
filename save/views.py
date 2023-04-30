from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'save/main.html')


def ticketfootball(request):
    return render(request,'save/football2.html')


def ticketcinema(request):
    return render(request,'save/cinema2.html')


def ticketplane(request):
    return render(request,'save/plane.html')