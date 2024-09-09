from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = 'workshop'

routers = DefaultRouter()
routers.register("products", ProductViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]