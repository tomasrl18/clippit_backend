from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]