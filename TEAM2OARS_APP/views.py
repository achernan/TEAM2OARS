from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Testimonies
from .models import Staff
from .models import Tenant
from .models import Tenant_Family
from .models import Invoices
from .models import Apartment
from .models import Automobiles
from .models import Handle_Rents
from .models import Complaints
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.safestring import SafeUnicode
from django.db.models import Count, Min, Sum, Avg

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
              invoices = Invoices.objects.filter(rental_no__exact=info.rental_no)
              R_num = SafeUnicode(info.rental_no)[12:] #removes rental number string for comparison
              rental = Handle_Rents.objects.filter(rental_no__exact=str(R_num))
              apartment = rental
              for apt in rental:
                A_num = SafeUnicode(apt.apt_no)[9:] #removes apt number string for comparison
                apartment = Apartment.objects.filter(apt_no__exact=A_num)
    
              automobiles = Automobiles.objects.filter(tenant_ss__exact=info.tenant_ss)
              family = Tenant_Family.objects.filter(tenant_ss__exact=info.tenant_ss)
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords,
                'invoices': invoices, 'apartment' : apartment,
                'automobiles': automobiles, 'allTenants' : allTenants,
                'family' : family, 'rental': rental
            }
        if context:
          return render(request, 'TEAM2OARS_APP/tenant_login.html', context)
        else:
          return render(request, 'TEAM2OARS_APP/front_page.html', {})

    if Staff.objects.filter(username__exact=request.POST['uname']):
        if Staff.objects.filter(password__exact=request.POST['pwd']):
            urecords = Staff.objects.filter(username__exact=request.POST['uname'])
            precords = Staff.objects.filter(password__exact=request.POST['pwd'])
            allInvoices = Invoices.objects.all()
            allStaff = Staff.objects.all()
            allAutomobiles = Automobiles.objects.all()
            autoCount = Automobiles.objects.values('auto_make').order_by().annotate(Count('auto_make'))
            staffCount = Handle_Rents.objects.values('staff_no').order_by().annotate(Count('staff_no'))
            allRents = Handle_Rents.objects.all()
            rentCount = Apartment.objects.aggregate(Sum('apt_rent_amt')).values()[0]
            allTenants = Tenant.objects.all()
            allApartments = Apartment.objects.all()
            allComplaints = Complaints.objects.all()
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords,
                'allTenants' : allTenants, 'allApartments' : allApartments,
                'allComplaints': allComplaints, 'allInvoices': allInvoices,
                'allRents': allRents, 'autoCount': autoCount,
                'allAutomobiles': allAutomobiles, 'rentCount': rentCount,
                'staffCount':staffCount, 'allStaff':allStaff
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

def create_rental(request):
    template = loader.get_template('TEAM2OARS_APP/assistant_login.html')
    urecords = Staff.objects.filter(username__exact='assistant1')
    allInvoices = Invoices.objects.all()
    allRents = Handle_Rents.objects.all()
    allTenants = Tenant.objects.all()
    allApartments = Apartment.objects.all()
    allComplaints = Complaints.objects.all()

    for s in urecords:
        staffNumber = s.staff_no

    aptNum = request.GET['availApartments']
    leaseType = request.GET['leaseType']

    tenantSS = request.GET['tenantSS']
    tenantName = request.GET['tenantName']
    tenantDOB = request.GET['tenantDOB']
    workPhone = request.GET['workPhone']

    content = Handle_Rents(apt_no=Apartment.objects.get(apt_no__exact=aptNum),
                           lease_type=leaseType,
                           rental_date=timezone.now(),
                           cancel_date='2016-06-02',
                           lease_start='2016-06-02',
                           lease_end='2017-06-02',
                           renewal_date='2017-06-01',
                           staff_no=Staff.objects.get(staff_no__exact=staffNumber))
    content.save()

    content2 = Tenant(tenant_ss=tenantSS,
                      tenant_name=tenantName,
                      tenant_DOB=tenantDOB,
                      work_phone=workPhone,
                      home_phone=workPhone,
                      username='tenant6',
                      password='tenant6#',
                      rental_no=Handle_Rents.objects.get(rental_no__exact='100106'))
    content2.save()

    Apartment.objects.filter(apt_no__exact=aptNum).update(apt_status='R')

    context = {
        'urecords': urecords, 'allTenants' : allTenants, 'allApartments' : allApartments,
        'allComplaints': allComplaints, 'allInvoices': allInvoices, 'allRents': allRents
    }

    return HttpResponse(template.render(context, request))

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
