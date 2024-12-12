import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Product name')
    category = django_filters.NumberFilter(field_name='category', lookup_expr='exact', label='Category ID')

    class Meta:
        model = Product
        fields = ['name', 'category']
