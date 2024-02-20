from django.urls import path
from api.views import EndPointDWH
# from .views import D_Sex_DWH, API_FClub, API_FLicence

urlpatterns = [
    path('api/end-point-dwh/', EndPointDWH.as_view(), name='end-point-dwh'),
    
    # path('api/d_sex/<str:sex_code>/', D_Sex_DWH.as_view(), name='d-sex-detail'),
    # path('api/f_club/', API_FClub.as_view(), name='api-f-club'),
    # path('api/f_club/<int:id>/', API_FClub.as_view(), name='api-f-club-detail'),
    # path('api/f_licence/', API_FLicence.as_view(), name='api-f-licence'),
    # path('api/f_licence/<int:id>/', API_FLicence.as_view(), name='api-f-licence-detail'),
]