#KNIGHT HACKS URLS
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('FinAssist.urls')),
    path('admin/', admin.site.urls),
]
