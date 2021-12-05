from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_notification_email(email, client, branch_id, address, equipment_type, replacement_date, days):
    context = {
        'email': email,
        'client': client,
        'branch_id': branch_id,
        'address': address,
        'equipment_type': equipment_type,
        'replacement_date': replacement_date,
        'days': days,
    }
    email_subject = 'Notification for Installation Replacement'
    email_body = render_to_string('users/emails/notification-mail.html', context)
    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    email.content_subtype = "html"
    return email.send(fail_silently=False)
