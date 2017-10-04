from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/added/
    url(r'^added$', views.added, name='added'),
]
