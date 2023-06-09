import django_filters

from .models import LostPost
from dogs.models import Dog

class OrderFilter(django_filters.FilterSet):

    age = django_filters.ChoiceFilter(label="Edad", choices=LostPost.Age.choices)
    sex = django_filters.ChoiceFilter(label="Sexo", choices=Dog.Sex.choices)
    size = django_filters.ChoiceFilter(label="Tamaño", choices=Dog.Size.choices)

    class Meta:
        model = LostPost
        fields = ['age', 'sex', 'color', 'size','breed']