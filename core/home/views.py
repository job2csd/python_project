from django.shortcuts import render,redirect # type: ignore

from django.http import HttpResponse # type: ignore
# Create your views here.

# Import the email utility function
from home.utils import send_email_to_client,send_email_with_attachment

from django.conf import settings

from .models import Car

def home(request):

    Car.objects.create(car_name="Ferrari",speed=200)

    #return HttpResponse("Welcome to the Home Page!")
    people_list = [{"name":"Maharshi Vyas","age":20},{"name":"jay vaghela","age":25},{"name":"Harsh vaghela","age":35}]
    return render(request, 'home/index.html',context={"peoples":people_list})


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

# View to trigger sending email
def send_email(request):
    #send_email_to_client()
    attachment = f'{settings.BASE_DIR}/email_attachment.pdf'
    send_email_with_attachment(
        subject="Test Email with Attachment",
        message="This is a test email sent from Django with an attachment.",
        recipient_list=["webspider943@gmail.com"],
        attachment_path=attachment
    )
    return redirect('/contact/')