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
    request.session.flush()
    return render(request, 'TEAM2OARS_APP/front_page.html', {})

def logout(request):
    request.session.flush()
    return render(request, 'TEAM2OARS_APP/front_page.html', {})

def login(request):
    return render(request, 'TEAM2OARS_APP/tenant_login.html', {'login': login})

def enter_credentials(request):
    request.session.load()

    if (request.session.load() == {}):
        request.session['uname'] = request.POST['uname']
        request.session['pwd'] = request.POST['pwd']


    #This is the code from before, that is not working now:
        #I'm not sure why it is not working anymore

    #request.session.load()

    #if (request.session.exists() == False):
        #request.session['uname'] = request.POST['uname']
        #request.session['pwd'] = request.POST['pwd']
        #print request.session['uname']

    #request.session.save() <-- this was messing up the new code, seemed to be deleting cookie instead of saving it


    if Tenant.objects.filter(username__exact=request.session['uname']):
        if Tenant.objects.filter(password__exact=request.session['pwd']):
            urecords = Tenant.objects.filter(username__exact=request.session['uname'])
            precords = Tenant.objects.filter(password__exact=request.session['pwd'])
            allTenants = Tenant.objects.all()
            for info in urecords:
                invoices = Invoices.objects.filter(rental_no__exact=info.rental_no)
                R_num = SafeUnicode(info.rental_no)[12:] #removes rental number string for comparison
                rental = Handle_Rents.objects.filter(rental_no__exact=str(R_num))
                apartment = rental
                for apt in rental:
                    A_num = SafeUnicode(apt.apt_no)[10:] #removes apt number string for comparison
                    apartment = Apartment.objects.filter(apt_no__contains=A_num)
                
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


    elif Staff.objects.filter(username__exact=request.session['uname']):
        if Staff.objects.filter(password__exact=request.session['pwd']):
            urecords = Staff.objects.filter(username__exact=request.session['uname'])
            precords = Staff.objects.filter(password__exact=request.session['pwd'])
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

    else:
        return render(request, 'TEAM2OARS_APP/front_page.html', {})

def about_us(request):
    return render(request, 'TEAM2OARS_APP/about_us.html', {'about': about_us})

def contact_us(request):
    return render(request, 'TEAM2OARS_APP/contact_us.html', {'contact': contact_us})


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

def submit_complaint(request):
    template = loader.get_template('TEAM2OARS_APP/tenant_login.html')
    username = request.GET['u']
    urecords = Tenant.objects.filter(username__exact=username)
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
        'urecords': urecords,
        'invoices': invoices, 'apartment' : apartment,
        'automobiles': automobiles, 'allTenants' : allTenants,
        'family' : family, 'rental': rental
    }

    complaint = request.GET['complaint']
    type = request.GET['type']
    rental_no = request.GET['rn']
    apt_no = request.GET['an']

    R_num = SafeUnicode(rental_no)[13:]
    A_num = SafeUnicode(apt_no)[10:]

    if type == 'rental':
        Complaints(complaint_date=timezone.now(),
                   rental_complaint=complaint,
                   rental_no=Handle_Rents.objects.get(rental_no__exact=str(R_num)),
                   apt_no=Apartment.objects.get(apt_no__exact=A_num)).save()
    elif type == 'apartment':
        Complaints(complaint_date=timezone.now(),
                   apt_complaint=complaint,
                   rental_no=Handle_Rents.objects.get(rental_no__exact=str(R_num)),
                   apt_no=Apartment.objects.get(apt_no__exact=A_num)).save()

    return HttpResponse(template.render(context, request))

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

    # use later possibly
    # tenantSS = request.GET['tenantSS']
    # tenantName = request.GET['tenantName']
    # tenantDOB = request.GET['tenantDOB']
    # workPhone = request.GET['workPhone']

    content = Handle_Rents(apt_no=Apartment.objects.get(apt_no__exact=aptNum),
                           lease_type=leaseType,
                           rental_date=timezone.now(),
                           cancel_date='2016-06-02',
                           lease_start='2016-06-02',
                           lease_end='2017-06-02',
                           renewal_date='2017-06-01',
                           staff_no=Staff.objects.get(staff_no__exact=staffNumber))
    content.save()

    Apartment.objects.filter(apt_no__exact=aptNum).update(apt_status='R')

    context = {
        'urecords': urecords, 'allTenants' : allTenants, 'allApartments' : allApartments,
        'allComplaints': allComplaints, 'allInvoices': allInvoices, 'allRents': allRents
    }

    return HttpResponse(template.render(context, request))

def new_tenant(request):
    tenantSS = request.GET['tenantSS']
    tenantName = request.GET['tenantName']
    tenantDOB = request.GET['tenantDOB']
    marital = request.GET['marital']
    workPhone = request.GET['workPhone']
    homePhone = request.GET['homePhone']
    employer = request.GET['employer']
    gender = request.GET['gender']

    Tenant(tenant_ss=tenantSS,
           tenant_name=tenantName,
           tenant_DOB=tenantDOB,
           marital=marital,
           work_phone=workPhone,
           home_phone=homePhone,
           employer=employer,
           gender=gender,
           username='tenant6',
           password='tenant6#',
           rental_no=Handle_Rents.objects.get(rental_no__exact='100106')).save()

    return render(request, 'TEAM2OARS_APP/front_page.html', {})


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
