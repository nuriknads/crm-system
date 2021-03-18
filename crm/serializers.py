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
