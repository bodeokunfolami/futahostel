from django.shortcuts import render
from . models import Hostel

def hostel_list(request):
    hostels = Hostel.objects.all()
    context = {
        'hostels': hostels
    }
    return render(request, 'hostels/list.html', context)
