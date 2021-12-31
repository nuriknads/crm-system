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
# Commit 25 — 2021-04-14
# Commit 27 — 2021-04-20
# Commit 46 — 2021-06-16
# Commit 49 — 2021-06-25
# Commit 51 — 2021-07-01
# Commit 67 — 2021-08-18
# Commit 5 — 2021-02-13
# Commit 6 — 2021-02-16
# Commit 11 — 2021-03-03
# Commit 12 — 2021-03-06
# Commit 14 — 2021-03-12
# Commit 20 — 2021-03-30
# Commit 21 — 2021-04-02
# Commit 22 — 2021-04-05
# Commit 24 — 2021-04-11
# Commit 27 — 2021-04-20
# Commit 36 — 2021-05-17
# Commit 38 — 2021-05-23
# Commit 40 — 2021-05-29
# Commit 47 — 2021-06-19
# Commit 48 — 2021-06-22
# Commit 55 — 2021-07-13
# Commit 59 — 2021-07-25
# Commit 70 — 2021-08-27
# Commit 72 — 2021-09-02
# Commit 81 — 2021-09-29
# Commit 83 — 2021-10-05
# Commit 85 — 2021-10-11
# Commit 88 — 2021-10-20
# Commit 95 — 2021-11-10
# Commit 99 — 2021-11-22
# Commit 100 — 2021-11-25
# Commit 102 — 2021-12-01
# Commit 104 — 2021-12-07
# Commit 107 — 2021-12-16
# Commit 110 — 2021-12-25
# Commit 111 — 2021-12-28
# Commit 112 — 2021-12-31
