from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
	url(r'^(?P<slug>[-\w]+)/$', views.post_page, name='post_page'),
]