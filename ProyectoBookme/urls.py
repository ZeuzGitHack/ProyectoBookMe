from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBookme/', include('AppBookme.urls')),
    path('UserBook/', include('UserBook.urls')),
]
