from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('texgine/', include('texgine.urls')),
    path('admin/', admin.site.urls), # What's this?
]