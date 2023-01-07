from django.views.generic.list import ListView
from .models import Menu


class MenuListView(ListView):
    model = Menu
