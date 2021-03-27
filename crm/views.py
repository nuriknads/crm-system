from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Client, Deal, Task
from .serializers import ClientSerializer, DealSerializer, TaskSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class DealViewSet(ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
# Commit 1 — 2021-02-01
# Commit 2 — 2021-02-04
# Commit 5 — 2021-02-13
# Commit 7 — 2021-02-19
# Commit 10 — 2021-02-28
# Commit 19 — 2021-03-27
