from django.shortcuts import render
from allcourses.models import Cour
# Create your views here.

def searchApp(request):
    searchTerm = request.GET.get('searchCourse')
    if searchTerm:
        courses = Cour.objects.filter(name__icontains=searchTerm)
        return render(request, 'searchApp.html',{'searchTerm':searchTerm, 'courses': courses})
    else:
        return render(request, 'searchAppZero.html')
    