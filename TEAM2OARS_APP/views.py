from django.shortcuts import render
from .models import Testimonies
from django.template import loader
from django.http import HttpResponse

def front_page(request):
    return render(request, 'TEAM2OARS_APP/front_page.html', {})

def about_us(request):
    return render(request, 'TEAM2OARS_APP/about_us.html', {'about': about_us})

def contact_us(request):
    return render(request, 'TEAM2OARS_APP/contact_us.html', {'contact': contact_us})

def testimonials(request):
    allTestimonies = Testimonies.objects.all()
    template = loader.get_template('TEAM2OARS_APP/testimonials.html')
    context = {
        'allTestimonies': allTestimonies
    }
    return HttpResponse(template.render(context, request))