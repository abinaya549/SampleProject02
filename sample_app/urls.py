from rest_framework.routers import DefaultRouter
from .views import StudentView
from django.urls import path, include

""" 
Model-view urls 
"""

# router = DefaultRouter()
# router.register('form', StudentView)
# urlpatterns = [
# path('api/', include(router.urls))

"""
urls for Api views
"""

urlpatterns = [
    # path('api/', include(router.urls))
    path('form/', StudentView.as_view()),
    path('form/<int:pk>', StudentView.as_view()),
]
