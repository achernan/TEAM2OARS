from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
    url(r'^about/$', views.about_us, name='about_us'),
    url(r'^Tenant/$', views.Tenant, name='Tenant'),
    url(r'^Assistant/$', views.Assistant, name='Assistant'),
    url(r'^Supervisor/$', views.Supervisor, name='Supervisor'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
    url(r'^testimonials/$', views.testimonials, name='testimonials')
]