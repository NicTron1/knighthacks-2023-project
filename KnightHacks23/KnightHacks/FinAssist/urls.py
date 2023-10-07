#THIS IS LOCATED IN FINASSIST

from django.urls import path
from . import views

urlpatterns = [
    path('FinAssist/', views.FinAssist, name='FinAssist'),
]
