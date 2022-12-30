from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('menu_tree/', include('menu_tree.urls')),
    path('admin/', admin.site.urls),
]