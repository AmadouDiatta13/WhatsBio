from django.urls import path
from . import views
from mycourse.views import deleteCourse

app_name = 'allcourses'

urlpatterns = [
    path('', views.Categories, name='categories'),
    path('<int:domaine_id>/', views.Lecons, name='lecons'),
    path('details/<int:cour_id>', views.Detail, name='detail'),
    path('details/<int:cour_id>/delete', deleteCourse, name='deletecourse'),
    path('<int:domaine_id>/create', views.CreateCour, name='createcour'),
]