from django import forms 
from .models import LostPost
from dogs.models import Dog


class LostPostForm (forms.ModelForm):



    class Meta: 
        model = LostPost
        fields = ('name', 'age', 'zone', 'sex', 'breed', 'color', 'size') 