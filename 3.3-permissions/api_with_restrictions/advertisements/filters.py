
from django_filters import FilterSet, DateFromToRangeFilter, ChoiceFilter
from advertisements.models import Advertisement


class AdvFilter(FilterSet):

    created_at = DateFromToRangeFilter()
    status = ChoiceFilter()
    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']

