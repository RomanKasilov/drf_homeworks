from django.db.models import QuerySet
from django.http import QueryDict

from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)

            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)

            case 'brand_start':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)

            case 'order_by':
                fields = CarSerializer.Meta.fields
                keys = [*fields, *[f'-{field}' for field in fields]]
                if v not in keys:
                    raise ValidationError({"error": f'Choose correct key for order_by.There are: {', '.join(keys)}'})
                qs = qs.order_by(v)

            case _:
                raise ValidationError(f'This filter for {k} not supported')
    return qs