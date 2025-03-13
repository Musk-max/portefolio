from django.shortcuts import render
from core.models import profiles

# Create your views here.
def index(request):
        Profiles=profiles.objects.all()
        return render(request, 'core/index.html', {
                'profiles':Profiles,
        })