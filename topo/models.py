from django.db import models

# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    type = models.CharField(max_length=50, default='device')  # e.g., router, switch, host
    metadata = models.JSONField(default=dict, blank=True)     # arbitrary attributes

    def __str__(self):
        return self.name

class Edge(models.Model):
    source = models.ForeignKey(Node, related_name='outgoing_edges', on_delete=models.CASCADE)
    target = models.ForeignKey(Node, related_name='incoming_edges', on_delete=models.CASCADE)
    bandwidth_mbps = models.FloatField(null=True, blank=True)
    latency_ms = models.FloatField(null=True, blank=True)
    directed = models.BooleanField(default=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(source=models.F('target')), name='no_self_loop'),
        ]

    def __str__(self):
        return f'{self.source} -> {self.target}'
