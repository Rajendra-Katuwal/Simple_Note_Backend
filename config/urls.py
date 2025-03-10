from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/auth/', include('authentication.urls')),
    path('notes/', include('notes.urls')),
]
