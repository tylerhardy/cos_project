import django_filters
from .models import Directory

class DirectoryListFilter(django_filters.FilterSet):
    """
    FilterView for searching assets
    """
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email_address = django_filters.CharFilter(lookup_expr='icontains')
    phone_number_1 = django_filters.CharFilter(lookup_expr='icontains')
    department = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Directory
        fields = ['first_name', 'last_name', 'email_address', 'phone_number_1', 'department', 'location', ]
        order_by = ['pk']