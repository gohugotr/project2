from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from product.models import Product
from .models import Setting, Contact, ContactForm

setting = Setting.objects.get(pk=1)

def index(request):
    # metin = 'Ali'
    # return HttpResponse('Merhaba %s' % metin)
    sliderdata=Product.objects.all()[:4]
    context = {'setting':setting,
               'page':'home',
               'sliderdata':sliderdata
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    context = {'setting':setting}
    return render (request,'hakkimizda.html',context)

def referanslar(request):
    context = {'setting': setting}
    return render(request,'referanslar.html',context)

def iletisim(request):

    if request.method == 'POST': # Form post edildiyse
        form = ContactForm(request.POST) # form post edildiyse
        if form.is_valid():
            data = Contact() # model ile bağlantı kur
            data.name    = form.cleaned_data['name'] # formdan bilgiyi al
            data.email   = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip      = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Mesajınız için teşekkür ederiz.')
            return HttpResponseRedirect('/iletisim')

    form = ContactForm() # form ile bağlantı kur
    context = {'setting': setting,'form':form}
    return render(request,'iletisim.html',context)


