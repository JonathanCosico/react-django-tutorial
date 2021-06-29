from django.urls import path
from .views import index

# when adding URLs, need to add to both this file and Django
urlpatterns = [
    path('', index),
    path('join', index),
    path('create', index),
    path('join/1', index)
]
