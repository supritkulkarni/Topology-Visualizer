from rest_framework import serializers
from .models import Node, Edge

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            'id',          # primary key
            'name',        # node name
            'ip_address',  # optional IP address
            'type',        # router, switch, host, etc.
            'metadata'     # JSON field for extra attributes
        ]


class EdgeSerializer(serializers.ModelSerializer):
    # Expose source/target IDs and names for convenience
    source = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all())
    target = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all())
    source_name = serializers.SerializerMethodField()
    target_name = serializers.SerializerMethodField()

    def get_source_name(self, obj):
        return obj.source.name

    def get_target_name(self, obj):
        return obj.target.name

    class Meta:
        model = Edge
        fields = [
            'id',
            'source',
            'target',
            'source_name',
            'target_name',
            'bandwidth_mbps',
            'latency_ms',
            'directed',
            'metadata'
        ]
