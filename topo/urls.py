from django.urls import path
from .views import TopologyView

urlpatterns = [
    path('', TopologyView.as_view(), name='topology'),
    
]
