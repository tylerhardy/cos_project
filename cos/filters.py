import django_filters
from .models import Asset

class AssetListFilter(django_filters.FilterSet):
    """
    FilterView for searching assets
    """
    class Meta:
        model = Asset
        fields = ['asset_tag', 'hardware_name', 'user', 'location', ]
        order_by = ['pk']