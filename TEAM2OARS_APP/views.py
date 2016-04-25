from django.shortcuts import render
from .models import Testimonies
from .models import Staff
from .models import Tenant
from .models import Invoices
from .models import Apartment
from .models import Automobiles
from django.template import loader
from django.http import HttpResponse

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
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords,
                'invoices': invoices, 'apartment' : apartment,
                'automobiles': automobiles, 'allTenants' : allTenants
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
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords,
                'allTenants' : allTenants, 'allApartments' : allApartments
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
