from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from .models import *
from django.db.models import Q
from .forms import SearchForm
from django.core.mail import send_mail

# Create your views here.



class CartView(ListView):
    template_name = 'search.html'
    model = Product
    context_object_name = 'objects'  # Set the context variable name



    def get_queryset(self):
        if self.request.GET.get('query')!=None:
            query=self.request.GET.get('query')
            objects = Product.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query)|Q(description__icontains=query)

                )
            return objects



class CreateFactor(View):

    def get(self,request,id):
        userr=Product.objects.get(id=id)
        createfactor=Factor.objects.create(user=request.user.username,product=userr.name)
        createfactor.save()

        return render(request,'send_email.html',{'createfactor':createfactor})
            

class SendEmail(View):

    def get(self,request):
        subject="confirm factor"
        message="factor is register"
        form_email="mr.mohammadrezanezhadfalah@gmail.com" 
        recive=request.user.email   
        send_mail(subject,message,form_email,[recive])

        return HttpResponse("send email")    
                