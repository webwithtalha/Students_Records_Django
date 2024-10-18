from django.shortcuts import render
from .models import Students

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records(request):
    students = Students.objects.get(id=1)
    return render(request, 'records.html', {'students': students})

def contact(request):
    return render(request, 'contact.html')