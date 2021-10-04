from django.urls import path
from .views import ContactViewSet

urlpatterns = [
    path('', ContactViewSet.as_view({'get': 'list', 'post': 'create'}), name='contacts'),
    path('<int:pk>/',
         ContactViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'}),
         name='contact'),
]
