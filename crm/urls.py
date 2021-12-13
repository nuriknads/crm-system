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
# Commit 1 — 2021-02-01
# Commit 28 — 2021-04-23
# Commit 60 — 2021-07-28
# Commit 61 — 2021-07-31
# Commit 64 — 2021-08-09
# Commit 69 — 2021-08-24
# Commit 77 — 2021-09-17
# Commit 106 — 2021-12-13
