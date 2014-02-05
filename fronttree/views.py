import datetime

from django import template
from django.shortcuts import render
from django.http import HttpResponse

from data.models import detector,reading,shot
from forms import contact_form

def gunshot_points(request):
    #TODO build information input here.

    shots = shot.objects.all()

    return render(request, 'mapstatic.html',{ "shots":shots},
                    content_type="application/xhtml+xml")

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = contact_form(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = contact_form() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
