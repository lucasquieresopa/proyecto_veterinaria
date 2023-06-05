import django_filters

from .models import AdoptionPost

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = AdoptionPost
        fields = ['age', 'sex', 'color']