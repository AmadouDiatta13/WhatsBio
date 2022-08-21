from django.db import models
from django.contrib.auth.models import User

class Domaine(models.Model):
    name = models.CharField(max_length=60, unique=True)
    image = models.ImageField(upload_to='images/Domaine', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
    
class Cour(models.Model):
    name = models.CharField(max_length=50)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/Cour', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/Cour', null= True, blank=True)
    document = models.FileField(upload_to='documents/Cour', null= True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    following = models.BooleanField(default= False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['create_date']