from home.models import *
import time
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Utility function to run tests
def run_tests():
    print("Function Started")
    print("Function Started..")
    time.sleep(2)
    print("Function Ended")

# Utility function to get all active vegetables
def send_email_to_client():
    subject="This is a Test Email"
    message="This is a test email sent from Django."
    email_from=settings.EMAIL_HOST_USER
    recipient_list=["webspider943@gmail.com"]
    send_mail( subject, message, email_from, recipient_list)

def send_email_with_attachment(subject, message, recipient_list, attachment_path):
    email_from = settings.EMAIL_HOST_USER
    email = EmailMessage(
        subject=subject, body=message, from_email=email_from, to=recipient_list)
    email.attach_file(attachment_path)
    email.send()