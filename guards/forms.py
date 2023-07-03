from django import forms
from .models import Guards
from django.core.validators import MaxValueValidator, MaxLengthValidator
from datetime import date


class GuardsRegisterForm(forms.ModelForm):
    vet = forms.CharField(
        label="Veterinaria", 
        required=True, 
        help_text="*",
        max_length=20,
    )

    address = forms.CharField(
        label="Dirreccion", 
        required=True, 
        help_text="*",
        max_length=15,
    )

    date_of_guards = forms.DateField(
        label="Día de guardia",
        required=True, 
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
    )

    class Meta:  
        model = Guards
        fields = ('vet', 'address','date_of_guards')
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(GuardsRegisterForm, self).__init__(*args, **kwargs)



    def clean(self):
        """Comprueba que no exista otro post con los mismos datos"""

        if self.is_valid():
            # actual_form_data = self.cleaned_data    #dict
            # user_adoption_posts = self.user.adoptionpost_set    #django many to many
            date_of_guards = self.cleaned_data['date_of_guards']

            if Guards.objects.filter( date_of_guards=date_of_guards).exists():
                raise forms.ValidationError("Ya existe una guardia para esta fecha ")
            
            return self.cleaned_data

class GuardsRegisterModificationForm(forms.ModelForm):
    vet = forms.CharField(
        label="Veterinaria", 
        required=True, 
        help_text="*",
        max_length=20,
    )

    address = forms.CharField(
        label="Dirreccion", 
        required=True, 
        help_text="*",
        max_length=15,
    )

    date_of_guards = forms.DateField(
        label="Día de guardia",
        required=True, 
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
    )

    class Meta:  
        model = Guards
        fields = ('vet', 'address','date_of_guards')
    
    


    def clean(self):
        """Comprueba que no exista otro post con los mismos datos"""

        if self.is_valid():
            # actual_form_data = self.cleaned_data    #dict
            # user_adoption_posts = self.user.adoptionpost_set    #django many to many

            date_of_guards = self.cleaned_data['date_of_guards']

            if Guards.objects.exclude(id=self.instance.id).filter( date_of_guards=date_of_guards).exists():
                raise forms.ValidationError("Ya existe una guardia con esa misma informacion")
            
            return self.cleaned_data
    
    def clean_vet(self):
        vet = self.cleaned_data['vet']
        return vet
        
    def clean_address(self):
        address = self.cleaned_data['address']
        return address
        
    def clean_date_of_guards(self):
        date_of_guards = self.cleaned_data['date_of_guards']
        return date_of_guards