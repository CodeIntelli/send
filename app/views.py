from django.shortcuts import render
# for normal email 
from django.core.mail import send_mail
from django.conf import settings

# now for template email 
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def home(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        print("*****************************************",to,content)

        # for normal message 
        # send_mail(subject, message, from_email, recipient_list)
        # send_mail('testing', content, settings.EMAIL_HOST_USER, [to])

        # now to sending template using email
        html_content = render_to_string('email.html',{'title':'Send Email Using Django','content':content,'to':to})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives('testing', content, settings.EMAIL_HOST_USER, [to])
        email.attach_alternative(html_content,'text/html')
        email.send()



        return render(request,'index.html',{'title':'Send Email Using Django'})
    else:
        return render(request,'index.html',{'title':'Send Email Using Django'})