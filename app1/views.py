from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home_view(req):
    if req.method == "POST":
        r_mail = req.POST.get('r_mail')
        subject = req.POST.get('subject')
        msg = req.POST.get('msg')

        rep_list = [r_mail]

        send_mail(subject, msg, settings.EMAIL_HOST_USER, rep_list)
        return HttpResponse('Mail sended')



    return render(req,'index.html')