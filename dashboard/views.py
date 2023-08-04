from django.shortcuts import render

from . models import Notes

# Create your views here.

def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    #recuperer les notes
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes}
    return render(request,'dashboard/notes.html',context)