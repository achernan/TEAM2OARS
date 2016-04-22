from django.shortcuts import render
from .models import Testimonies
from .models import Staff
from .models import Tenant
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
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords
            }

    if Staff.objects.filter(username__exact=request.POST['uname']):
        if Staff.objects.filter(password__exact=request.POST['pwd']):
            urecords = Staff.objects.filter(username__exact=request.POST['uname'])
            precords = Staff.objects.filter(password__exact=request.POST['pwd'])
            context = {
                'urecords': urecords, 'query': urecords,
                'precords': precords, 'query': precords
            }

    if context:
        return render(request, 'TEAM2OARS_APP/tenant_login.html', context)
    else:
        return render(request, 'TEAM2OARS_APP/front_page.html', {})



def about_us(request):
    return render(request, 'TEAM2OARS_APP/about_us.html', {'about': about_us})

def contact_us(request):
    return render(request, 'TEAM2OARS_APP/contact_us.html', {'contact': contact_us})

def login(request):
    return render(request, 'TEAM2OARS_APP/tenant_login.html', {'login': login})

def testimonials(request):
    return render(request, 'TEAM2OARS_APP/testimonials.html', {'testimonials': testimonials})

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

