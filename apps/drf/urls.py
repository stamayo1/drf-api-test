from django.urls import path
from .views import *

urlpatterns = [
    path('enterprises/', EnterpriseAPIView.as_view()),
    path('enterprises/<int:pk>/', DetailEnterpriseAPIView.as_view()),
    path('enterprises/<int:pk>/list-code', EnterpriseCodeAPIView.as_view()),
    path('enterprises/nit/<int:nit>/', EnterpriseNitAPIView.as_view()),
    path('codes/', CodeAPIView.as_view()),
    path('codes/<int:pk>/', DetailCodeAPIView.as_view()),
    path('codes/<int:pk>/owner', CodeOwnerAPIView.as_view()),
]
