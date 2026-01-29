from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def booking_list(request):
    return HttpResponse("List of bookings")