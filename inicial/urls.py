from django.conf.urls import url
from . import views

app_name = 'inicial'

urlpatterns = [
    #
    url(r'^$', views.IndexView.as_view(), name='index'),
]