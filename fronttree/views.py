import datetime

from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from data.models import device,channel,sample
from forms import contact_form

def readings(request):
    #TODO build information input here.

    samples = sample.objects.all()
    samplejson =[]
    for i in samples:
        samplejson.append(i.tojson())

    return render(request, 'readings.html',{ "samples":str(samplejson)},
                    content_type="application/xhtml+xml")

@csrf_exempt
def reading(request):
    #TODO build information input here.
    data = []

    get= []
    for key, value in request.GET.iteritems():
        get.append({key:value})
    data.append({'get':get})

    data.append({'body':request.body})

    post=[]
    for key in request.POST:
        post.append({str(key):request.POST.get(key)})

    for key, value in request.POST.iteritems():
        post.append({key:value})
    data.append({'post':post})

    json = str({'success':True, 'postbody': data,"post":str(request.POST)})
    return HttpResponse(json, mimetype='application/json')

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
