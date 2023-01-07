from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Menu


class MenuListView(ListView):
    model = Menu


class MenuDetailView(DetailView):
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = Menu.objects.all()
        obj = super().get_object()
        context['children'] = Menu.objects.filter(parent_id=obj.id)

        return context