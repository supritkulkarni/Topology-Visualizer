from rest_framework import viewsets
from rest_framework.response import Response
from .models import Node, Edge
from .serializers import NodeSerializer, EdgeSerializer
from rest_framework.decorators import api_view

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().order_by('name')
    serializer_class = NodeSerializer

class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.select_related('source', 'target').all()
    serializer_class = EdgeSerializer

@api_view(['GET'])
def graph_elements(request):
    nodes = Node.objects.all()
    edges = Edge.objects.select_related('source', 'target').all()

    cy_nodes = [
        {
            'data': {
                'id': str(n.id),
                'label': n.name,
                'type': n.type,
                **n.metadata
            }
        }
        for n in nodes
    ]

    cy_edges = [
        {
            'data': {
                'id': f'e{e.id}',
                'source': str(e.source_id),
                'target': str(e.target_id),
                'label': f'{e.source.name} → {e.target.name}',
                'bandwidth_mbps': e.bandwidth_mbps,
                'latency_ms': e.latency_ms,
                'directed': e.directed,
                **e.metadata
            }
        }
        for e in edges
    ]

    return Response({'elements': cy_nodes + cy_edges})