from django.urls import path
from . import views
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('api/sensor/<int:pk>/', views.SensorView.as_view()),
    path('api/measurements/', views.MeasurementView.as_view()),
    path('api/sensors/', views.SensorsView.as_view()),
]
