from datetime import date
from django import forms
from .models import Campaign


class CampaignForm(forms.ModelForm):
    image = forms.ImageField(
        label="Foto para la colecta",
        required=True,
        help_text="*",
    )
    campaign_name = forms.CharField(
        label="Nombre de la colecta", 
        required=True, 
        help_text="*",
        max_length=30,
    )
    description = forms.CharField(
        label="Descripción de la colecta", 
        required=False,
        max_length=120,
    )
    target_date = forms.DateField(
        label="Fecha objetivo",
        required=True,
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),  
    )
    target_money = forms.IntegerField(
        label="Dinero objetivo",
        min_value=1,
        required=True, 
        help_text="*",
        max_value=999999,
    )
 
    class Meta: 
        model = Campaign
        fields = ('image', 'campaign_name', 'description', 'target_date', 'target_money') 

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(CampaignForm, self).__init__(*args, **kwargs)


    def clean_date_of_shift(self):
        if self.is_valid():
            target_date = self.cleaned_data['target_date']
 
            if target_date <= date.today():
                raise forms.ValidationError('Debe elegir una fecha posterior a la fecha de hoy')
            else:
                return self.cleaned_data['target_date']
            
    def clean_target_money(self):
        if self.is_valid():
            target_money = self.cleaned_data['target_money']

            if target_money < 50:
                raise forms.ValidationError('El dinero objetivo debe ser mayor a 50 dolares')
            else: 
                return self.cleaned_data['target_money']
            

    def clean(self):
        """Comprueba que no exista otro post con los mismos datos"""

        if self.is_valid():
            # actual_form_data = self.cleaned_data    #dict
            # user_adoption_posts = self.user.adoptionpost_set    #django many to many
            campaign_name = self.cleaned_data['campaign_name']
            description = self.cleaned_data['description']
            target_date = self.cleaned_data['target_date']
            target_money = self.cleaned_data['target_money']

            if self.user.campaign_set.filter(campaign_name=campaign_name, description=description, 
                                        target_date=target_date, target_money=target_money):
                raise forms.ValidationError("Ya existe una colecta con exactamente la misma información")
            
            return self.cleaned_data
        

class CampaignModificationForm(forms.ModelForm):

    image = forms.ImageField(
        label="Foto para la colecta",
        required=True,
        help_text="*",
    )
    campaign_name = forms.CharField(
        label="Nombre de la colecta", 
        required=True, 
        help_text="*",
        max_length=30,
    )
    description = forms.CharField(
        label="Descripción de la colecta", 
        required=False,
        max_length=120,
    )
    target_date = forms.DateField(
        label="Fecha objetivo",
        required=True,
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),  
    )
    target_money = forms.IntegerField(
        label="Dinero objetivo",
        min_value=1,
        required=True, 
        help_text="*",
        max_value=999999,
    )
 
    class Meta: 
        model = Campaign
        fields = ('campaign_name', 'description', 'target_date', 'target_money', 'image' ) 

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(CampaignModificationForm, self).__init__(*args, **kwargs)
        self.initial['target_date'] = self.instance.target_date.isoformat()


    def clean_date_of_shift(self):
        if self.is_valid():
            target_date = self.cleaned_data['target_date']
 
            if target_date <= date.today():
                raise forms.ValidationError('Debe elegir una fecha posterior a la fecha de hoy')
            else:
                return self.cleaned_data['target_date']
            
    def clean_target_money(self):
        if self.is_valid():
            target_money = self.cleaned_data['target_money']

            if target_money < 50:
                raise forms.ValidationError('El dinero objetivo debe ser mayor a 50 dolares')
            else: 
                return self.cleaned_data['target_money']
            

    def clean(self):
        """Comprueba que no exista otro post con los mismos datos"""

        if self.is_valid():
            # actual_form_data = self.cleaned_data    #dict
            # user_adoption_posts = self.user.adoptionpost_set    #django many to many
            campaign_name = self.cleaned_data['campaign_name']
            description = self.cleaned_data['description']
            target_date = self.cleaned_data['target_date']
            target_money = self.cleaned_data['target_money']

            if self.user.campaign_set.filter(campaign_name=campaign_name, description=description, 
                                        target_date=target_date, target_money=target_money).exclude(id=self.instance.id):
                raise forms.ValidationError("Ya posee una colecta con exactamente la misma información")
            
            return self.cleaned_data
    
    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     return image
    
    def clean_campaign_name(self):
        campaign_name = self.cleaned_data['campaign_name']
        return campaign_name

    def clean_description(self):
        description = self.cleaned_data['description']
        return description

    def clean_target_date(self):
        target_date = self.cleaned_data['target_date']
        return target_date

    def clean_target_money(self):
        target_money = self.cleaned_data['target_money']
        return target_money