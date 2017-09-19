from django.views import generic
from .models import Parceiro

class IndexView(generic.ListView):
    template_name = 'inicial/index.html'
    context_object_name = 'todos_parceiros'

    def get_queryset(self):
        return Parceiro.objects.all()

