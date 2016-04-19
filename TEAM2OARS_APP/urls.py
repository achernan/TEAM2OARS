from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
    url(r'^about/$', views.about_us, name='about_us'),
    url(r'^login/$', views.login, name='tenant_login'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
    url(r'^testimonials/$', views.testimonials, name='testimonials'),
    url(r'^search/$', views.search, name='search')
]