from django.urls import path
from .views import MenuListView, MenuDetailView


urlpatterns = [
    path('', MenuListView.as_view(), name='index'),
    path('<int:slug>/', MenuDetailView.as_view(), name='menu')
]