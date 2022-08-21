from django.shortcuts import render, redirect, get_object_or_404
from .models import Domaine, Cour
from .forms import CreateCourForm

def Categories(request):
    categories = Domaine.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def Lecons(request, domaine_id):
    domaine = get_object_or_404(Domaine, pk=domaine_id)
    lecons = Cour.objects.filter(domaine = domaine)
    return render(request, 'lecons.html', {'domaine': domaine, 'lecons':lecons})

def Detail(request, cour_id):
    cour = get_object_or_404(Cour,pk=cour_id)
    return render(request, 'detail.html',{'cour':cour})

def CreateCour(request, domaine_id):
    domaine = get_object_or_404(Domaine, pk=domaine_id)
    
    if request.method == 'GET':
        return render(request, 'createcour.html', {'form': CreateCourForm(), 'domaine': domaine})
    else:
        try:
            form = CreateCourForm(request.POST, request.FILES)
            newCour = form.save(commit=False)
            newCour.user = request.user
            newCour.domaine = domaine
            newCour.save()
            return redirect('allcourses:lecons', newCour.domaine.id)
        except ValueError:
            return redirect(request, 'createcour.html', {'form':CreateCourForm(), 'error':'Donnees invalides'})

         