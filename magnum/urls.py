from django.urls import path
from magnum.views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'}), name='users'),
]
