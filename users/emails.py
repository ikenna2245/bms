from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_registration_email(email, password, first_name):
    context = {
        'email': email,
        'password': password,
        'first_name': first_name
    }
    email_subject = 'Prostar Global Energy Account Created'
    email_body = render_to_string('users/emails/welcome-mail.html', context)
    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    email.content_subtype = "html"
    return email.send(fail_silently=False)
