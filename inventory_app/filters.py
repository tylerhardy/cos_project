import django_filters
from .models import Asset

class AssetListFilter(django_filters.FilterSet):
    """
    FilterView for searching assets
    """
    asset_tag = django_filters.CharFilter(lookup_expr='icontains')
    hardware_name = django_filters.CharFilter(lookup_expr='icontains')
    user = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Asset
        fields = ['asset_tag', 'hardware_name', 'user', 'location', ]
        order_by = ['pk']