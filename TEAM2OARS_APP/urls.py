from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.front_page, name='front_page'),
    url(r'^enter_credentials/$', views.enter_credentials, name='enter_credentials'),
    url(r'^save_testimonial/$', views.save_testimonial, name='save_testimonial'),
    url(r'^update_status/$', views.update_status, name='update_status'),
    url(r'^about/$', views.about_us, name='about_us'),
    url(r'^tenantWelcome/$', views.login, name='tenant_login'),
    url(r'^assistantLogin/$', views.assistantLogin, name='assistant_login'),
    url(r'^managerLogin/$', views.managerLogin, name='manager_login'),
    url(r'^supervisorLogin/$', views.supervisorLogin, name='supervisor_login'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
    url(r'^testimonials/$', views.testimonials, name='testimonials'),
    #url(r'^tenantslist/$', views.tenantslist, name='tenantslist'),
    url(r'^search/$', views.search, name='search')
]