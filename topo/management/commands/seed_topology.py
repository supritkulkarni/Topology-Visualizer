from django.core.management.base import BaseCommand
from topo.models import Node, Edge

class Command(BaseCommand):
    help = 'Seed sample topology data'

    def handle(self, *args, **kwargs):
        Node.objects.all().delete()
        Edge.objects.all().delete()

        r = Node.objects.create(name='Router-1', type='router', metadata={'vendor': 'Cisco'})
        s = Node.objects.create(name='Switch-1', type='switch', metadata={'ports': 24})
        h1 = Node.objects.create(name='Host-1', type='device', ip_address='10.0.0.10')
        h2 = Node.objects.create(name='Host-2', type='device', ip_address='10.0.0.11')

        Edge.objects.create(source=r, target=s, bandwidth_mbps=1000, latency_ms=1, directed=True)
        Edge.objects.create(source=s, target=h1, bandwidth_mbps=100, latency_ms=2, directed=False)
        Edge.objects.create(source=s, target=h2, bandwidth_mbps=100, latency_ms=2, directed=False)

        self.stdout.write(self.style.SUCCESS('Seeded topology'))
