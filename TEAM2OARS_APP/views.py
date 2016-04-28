from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Testimonies
from .models import Staff
from .models import Tenant
from .models import Tenant_Family
from .models import Invoices
from .models import Apartment
from .models import Automobiles
from .models import Complaints
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def front_page(request):
    return render(request, 'TEAM2OARS_APP/front_page.html', {})

def enter_credentials(request):
    context = False

    if Tenant.objects.filter(username__exact=request.POST['uname']):
        if Tenant.objects.filter(password__exact=request.POST['pwd']):
            urecords = Tenant.objects.filter(username__exact=request.POST['uname'])
            precords = Tenant.objects.filter(password__exact=request.POST['pwd'])
            allTenants = Tenant.objects.all()
            for info in urecords:
              invoices = Invoices.objects.filter(tenant_ss__exact=info.tenant_ss)
              apartment = Apartment.objects.filter(tenant_ss__exact=info.tenant_ss)
              automobiles = Automobiles.objects.filter(tenant_ss__exact=info.tenant_ss)
              family = Tenant_Family.objects.filter(tenant_ss__exact=info.tenant_ss)
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords,
                'invoices': invoices, 'apartment' : apartment,
                'automobiles': automobiles, 'allTenants' : allTenants,
                'family' : family
            }
        if context:
          return render(request, 'TEAM2OARS_APP/tenant_login.html', context)
        else:
          return render(request, 'TEAM2OARS_APP/front_page.html', {})

    if Staff.objects.filter(username__exact=request.POST['uname']):
        if Staff.objects.filter(password__exact=request.POST['pwd']):
            urecords = Staff.objects.filter(username__exact=request.POST['uname'])
            precords = Staff.objects.filter(password__exact=request.POST['pwd'])
            allTenants = Tenant.objects.all()
            allApartments = Apartment.objects.all()
            allComplaints = Complaints.objects.all()
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords,
                'allTenants' : allTenants, 'allApartments' : allApartments,
                'allComplaints': allComplaints
            }
            if urecords.filter(position__contains='supervisor'):
              if context:
                return render(request, 'TEAM2OARS_APP/supervisor_login.html', context)
            if urecords.filter(position__contains="manager"):
              if context:
                return render(request, 'TEAM2OARS_APP/manager_login.html', context)
            if urecords.filter(position__contains="assistant"):
              if context:
                return render(request, 'TEAM2OARS_APP/assistant_login.html', context)
              
        return render(request, 'TEAM2OARS_APP/front_page.html', {})

def about_us(request):
    return render(request, 'TEAM2OARS_APP/about_us.html', {'about': about_us})

def contact_us(request):
    return render(request, 'TEAM2OARS_APP/contact_us.html', {'contact': contact_us})

def login(request):
    return render(request, 'TEAM2OARS_APP/tenant_login.html', {'login': login})


def testimonials(request):
    return render(request, 'TEAM2OARS_APP/testimonials.html', {'testimonials': testimonials})

#def assistantLogin(request):
 #   return render(request, 'TEAM2OARS_APP/assistant_login.html', {'assistantLogin': assistantLogin})

def save_testimonial(request):
    content = request.POST.get('c')
    userdata = request.POST.get('social')
    content_object = Testimonies(testimonial_date=timezone.now(),
                                 testimonial_content=content,
                                 tenant_ss=Tenant.objects.get(tenant_ss__exact=userdata))
    content_object.save()
    return HttpResponseRedirect('/testimonials/')

def update_status(request): # of complaints to Fixed
    template = loader.get_template('TEAM2OARS_APP/supervisor_login.html')
    urecords = Staff.objects.filter(username__exact='supervisor')
    allApartments = Apartment.objects.all()
    allComplaints = Complaints.objects.all()
    allTenants = Tenant.objects.all()
    context = {
        'urecords': urecords,
        'allApartments': allApartments,
        'allComplaints': allComplaints,
        'allTenants': allTenants
    }
    if Complaints.objects.get(complaint_id__exact=request.GET['cn']):
        Complaints.objects.filter(complaint_id__exact=request.GET['cn']).update(status='F')
        return HttpResponse(template.render(context, request))

    else:
        return HttpResponse("invalid complaint number")

def search(request):
    allTestimonies = Testimonies.objects.filter(testimonial_content__contains=request.GET['q'])
    template = loader.get_template('TEAM2OARS_APP/search.html')
    if Testimonies.objects.count > 1:
        context = {
            'allTestimonies': allTestimonies
        }
        return HttpResponse(template.render(context, request))
    elif Testimonies.objects.count < 1:
        return HttpResponse(template.render({'allTestimonies': allTestimonies}, request))

def assistantLogin(request):
    allTenants = Tenant.objects.all()
    template = loader.get_template('TEAM2OARS_APP/assistant_login.html')
    if Tenant.objects.count > 1:
        context = {
            'allTenants': allTenants
        }
        return HttpResponse(template.render(context, request))
    elif Tenant.objects.count < 1:
        return HttpResponse(template.render({'allTenants': allTenants}, request))

def managerLogin(request):
    allTenants = Tenant.objects.all()
    template = loader.get_template('TEAM2OARS_APP/manager_login.html')
    if Tenant.objects.count > 1:
        context = {
            'allTenants': allTenants
        }
        return HttpResponse(template.render(context, request))
    elif Tenant.objects.count < 1:
        return HttpResponse(template.render({'allTenants': allTenants}, request))
        
def supervisorLogin(request):
    allTenants = Tenant.objects.all()
    template = loader.get_template('TEAM2OARS_APP/supervisor_login.html')
    if Tenant.objects.count > 1:
        context = {
            'allTenants': allTenants
        }
        return HttpResponse(template.render(context, request))
    elif Tenant.objects.count < 1:
        return HttpResponse(template.render({'allTenants': allTenants}, request))
