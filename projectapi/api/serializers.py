from rest_framework import serializers
from .models import BryUser, Ttdphw016100, Ttdphw016200


class BryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BryUser
        fields = '__all__'


class FirstCompanyrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ttdphw016100
        fields = '__all__'


class Ttdphw016200Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ttdphw016200
        fields = '__all__'
