from django.urls import path
from .views import MenuListView, MenuDetailView


urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('<slug:slug>/', MenuDetailView.as_view(), name='menu')
]