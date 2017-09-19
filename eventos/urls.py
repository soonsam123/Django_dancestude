from django.conf.urls import url
from . import views

app_name = 'eventos'

urlpatterns = [
    # eventos/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # eventos/71...
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]


