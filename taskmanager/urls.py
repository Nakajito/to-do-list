from django.contrib import admin
from django.urls import path, include
from .views import index
from tasks import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tasks/', include('tasks.urls')),
]
