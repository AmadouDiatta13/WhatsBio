from django.shortcuts import render, redirect, get_object_or_404
from allcourses.models import Cour


def mycourse(request):
        try:
                mescours = Cour.objects.filter(user_id=request.user)
                return render(request, 'mycourse.html', {'mescours':mescours})
        except:
                return render(request, 'mycoursesanspermi.html')

def deleteCourse(request, cour_id):
    cour = get_object_or_404(Cour, pk=cour_id)
    cour.delete()
    return redirect('mycourses')   