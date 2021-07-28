from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, DealViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'deals', DealViewSet, basename='deal')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
# Commit 18 — 2021-03-24
# Commit 38 — 2021-05-23
# Commit 60 — 2021-07-28
