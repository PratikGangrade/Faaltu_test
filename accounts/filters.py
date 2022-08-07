from dataclasses import field
import django_filters as dj
from .models import *
from django_filters import DateFilter

class OrderFilter(dj.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr="gte")
    end_date = DateFilter(field_name='date_created', lookup_expr="lte")
    class Meta:
        model = order
        fields = '__all__'
        exclude = ('customer', 'date_created')
