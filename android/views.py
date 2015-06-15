from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from android.models import Document

def home(request):
    data={}
    return render_to_response('index.html',data,context_instance=RequestContext(request))


def about(request):
    data = {}
    documents = Document.objects.all()
    data['documents'] =documents
    return render_to_response('about.html',data,context_instance=RequestContext(request))

def portfolio(request):
    data={}
    return render_to_response('portfolio.html',data,context_instance=RequestContext(request))

def clients(request):
    data={}
    return render_to_response('clients.html',data,context_instance=RequestContext(request))

def contacts(request):
    print"ddddddddddd"
    if request.method == 'POST': # If the form has been submitted...
        print"rrrrrrrrrrr"
        name = request.POST['fullname']
        user_mail = request.POST['email']
        subject = "  Telephone: "+request.POST['telephone']+"  from: "+user_mail
        message = request.POST['message']
        sender = 'rajmohan@doublespring.com'
        recipients = ['rajmohanjr@gmail.com']
        #cc_myself = request.POST['date']['cc_myself']

#        recipients = ['rajmohan@doublespring.com']
#        if cc_myself:
#            recipients.append(sender)

        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients)
        return render_to_response('success_mail.html',context_instance=RequestContext(request))
    else:
        return render_to_response('contacts.html',context_instance=RequestContext(request))




def file_download(request,pk=0):
    doc = Document.objects.distinct().get(id=pk)
    fname=doc.docfile.name
    print"SSSSSSsssss",fname
    import urllib;   
    url ="http://127.0.0.1:8000/media/"+fname
    print"url",url
    try:
        opener = urllib.urlopen(url);
    except:
        import sys
        print sys.exc_info()  
    mimetype = "application/octet-stream"
    response = HttpResponse(opener.read(), mimetype=mimetype)
    response["Content-Disposition"]= "attachment; filename=aktel.jpg"
    return response 