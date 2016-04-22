from django.shortcuts import render

def front_page(request):
    return render(request, 'TEAM2OARS_APP/front_page.html', {})

def about_us(request):
    return render(request, 'TEAM2OARS_APP/about_us.html', {'about': about_us})

def contact_us(request):
    return render(request, 'TEAM2OARS_APP/contact_us.html', {'contact': contact_us})

def Tenant(request):
    return render(request, 'TEAM2OARS_APP/tenant_login.html', {'Tenant': Tenant})
    
def Assistant(request):
    return render(request, 'TEAM2OARS_APP/assistant_login.html', {'Assistant': Assistant})
    
def Supervisor(request):
    return render(request, 'TEAM2OARS_APP/supervisor_login.html', {'Supervisor': Supervisor})

def testimonials(request):
    return render(request, 'TEAM2OARS_APP/testimonials.html', {'testimonials': testimonials})