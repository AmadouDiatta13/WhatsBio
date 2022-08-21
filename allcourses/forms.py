from django.forms import ModelForm, Textarea, TextInput
from .models import Cour

class CreateCourForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget
        self.fields['video'].widget
        self.fields['document'].widget
        
    class Meta:
        model = Cour
        fields = ['name', 'description', 'image', 'video', 'document']
        widgets = {
            'description': Textarea(attrs={'rows':4}),       
        }