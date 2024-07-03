# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorsDetailSerializer

class SensorView(APIView):

    def put(self,request,pk):
        sensor = Sensor.objects.get(pk='pk')
        serializer = SensorSerializer(sensor,data=request.data)
        serializer.save()
        return Response(serializer.data)

    def post(self,request):
        serializer = SensorSerializer(data=request.data)
        serializer.save()
        return Response(serializer.data)


class SensorsDetailView(APIView):
    def get(self,request):
        sensors = Sensor. objects.all()
        serializer = SensorsDetailSerializer(sensors, many=True)
        return Response(serializer.data)

class MeasurementView(APIView):
    def post(self,request):
        serializer = MeasurementSerializer(data=request.data)
        serializer.save()
        return Response(serializer.data)

