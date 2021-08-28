from django.shortcuts import render
from django.views import View
from django.conf import settings
from .models import Destination
class HomeView(View):
    def get(self, request):
        dests = Destination.objects.all()
        return render(request, 'home/main.html', {'dests': dests})

