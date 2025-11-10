from django.contrib import admin
from .models import Node, Edge

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'type')
    search_fields = ('name', 'ip_address', 'type')

@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ('source', 'target', 'bandwidth_mbps', 'latency_ms', 'directed')
    list_filter = ('directed',)
    search_fields = ('source__name', 'target__name')
