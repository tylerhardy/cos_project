import django_filters
from django_filters import DateFromToRangeFilter, DateFilter, CharFilter, NumberFilter, ModelChoiceFilter, ModelMultipleChoiceFilter
from django_filters.widgets import RangeWidget
from .models import Post

class JournalListFilter(django_filters.FilterSet):
    """
    FilterView for searching journal_app entries
    """
    title = CharFilter(lookup_expr='icontains')
    text = CharFilter(lookup_expr='icontains')
    # published_date = DateFilter(lookup_expr='year__gte')
    # published_date = DateFromToRangeFilter(label='Published Date Range',widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'published_date',]
        order_by = ['published_date']