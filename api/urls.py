from django.urls import path
from api.views import EndPointDWH

urlpatterns = [
    path('api/end-point-dwh/', EndPointDWH.as_view(), name='end-point-dwh'),
]