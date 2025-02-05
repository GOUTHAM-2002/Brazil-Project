from django.urls import path
from . import views
from .views import generate_content

urlpatterns = [
     path('generate_content/', generate_content, name='generate_content'),
]
