from rest_framework.routers import DefaultRouter
from .views import StudentView
from django.urls import path, include

router = DefaultRouter()
router.register('form', StudentView)

urlpatterns = [
    path('api/', include(router.urls))
]
