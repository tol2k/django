from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы



class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id','temrerature']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id','name','description']

class SensorsDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id','name','description','measurements']