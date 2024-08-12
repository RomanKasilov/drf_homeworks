from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'photo')

    # def validate(self, data):
    #     if data['price'] == data['year']:
    #         raise ValidationError({'details': 'fields price and year are the same'})
    #     return data
    #
    # def validate_year(self, year):
    #     if year == 2024:
    #         raise ValidationError({'details': 'year = 2024 is forbidden'})
    #     return year


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}

