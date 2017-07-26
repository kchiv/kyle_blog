from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
	url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', views.post_page, name='post_page'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.category_page, name='category_page'),
]