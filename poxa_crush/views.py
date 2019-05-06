from django.shortcuts import render
from poxa_crush.models import Crush
# Create your views here.

def index (request):
    crushs = Crush.objects.all()
    contexto = {
        'crushs' : crushs
    }
    return render(request, 'index.html', contexto)