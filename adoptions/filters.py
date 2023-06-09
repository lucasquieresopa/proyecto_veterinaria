import django_filters

from .models import AdoptionPost
from dogs.models import Dog

class OrderFilter(django_filters.FilterSet):

    age = django_filters.ChoiceFilter(label="Edad", choices=AdoptionPost.Age.choices)
    sex = django_filters.ChoiceFilter(label="Sexo", choices=Dog.Sex.choices)
    size = django_filters.ChoiceFilter(label="Tamaño", choices=Dog.Size.choices)

    class Meta:
        model = AdoptionPost
        fields = ['age', 'sex', 'color', 'size']
