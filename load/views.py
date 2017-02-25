from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from forms import Complaintform
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("<h1> This is the home page</h1>")

def complain(request):
    if request.POST:
        form=Complaintform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/load/complaint')
    else:
        form=Complaintform()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('complain.html',args)