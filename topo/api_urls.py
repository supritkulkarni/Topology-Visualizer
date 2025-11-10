from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import NodeViewSet, EdgeViewSet, graph_elements

router = DefaultRouter()
router.register(r'nodes', NodeViewSet)
router.register(r'edges', EdgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('graph/', graph_elements, name='graph-elements')

]
