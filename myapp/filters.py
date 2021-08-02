import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(lookup_expr='icontains')
    prenom = django_filters.CharFilter(lookup_expr='icontains')
    function = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employee