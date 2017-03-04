from rest_framework import serializers

from hotelapp.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=('id','name','wilaya','address')