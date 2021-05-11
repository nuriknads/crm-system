from rest_framework import serializers
from .models import Client, Deal, Task

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    deals = DealSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'company', 'created_at', 'deals', 'tasks']
# Commit 3 — 2021-02-07
# Commit 12 — 2021-03-06
# Commit 16 — 2021-03-18
# Commit 17 — 2021-03-21
# Commit 24 — 2021-04-11
# Commit 35 — 2021-05-14
# Commit 43 — 2021-06-07
# Commit 44 — 2021-06-10
# Commit 45 — 2021-06-13
# Commit 68 — 2021-08-21
# Commit 10 — 2021-02-28
# Commit 16 — 2021-03-18
# Commit 34 — 2021-05-11
