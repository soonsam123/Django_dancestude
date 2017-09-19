from django.views import generic
from .models import Evento

class IndexView(generic.ListView):
    template_name = 'eventos/index.html'
    context_object_name = 'todos_eventos'

    def get_queryset(self):
        return Evento.objects.all()

class DetailView(generic.DetailView):
    model = Evento
    template_name = 'eventos/detail.html'



