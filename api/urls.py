from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, TaskViewSet, RegisterView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]