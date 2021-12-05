from celery.utils.log import get_task_logger
from celery import shared_task
from django.conf import settings      
from twilio.rest import Client
from django.utils import timezone
import datetime as DT
from .models import Installation
from .emails import send_notification_email

logger = get_task_logger(__name__)

@shared_task
def sendReplacementNotification():
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    info = Installation.objects.all()
    for i in info:
        if i.replacement_date:
            week_ago = i.replacement_date - DT.timedelta(7)
            day_2_ago = i.replacement_date - DT.timedelta(2)
            email_info = { 'email' : i.location.clients.email,
                'client': i.location.clients.first_name,
                'branch_id' : i.location.branch_id,
                'address' : i.location.address,
                'equipment_type' : i.get_equipment_type_display(),
                'replacement_date' : i.replacement_date }
            if timezone.now().date() == week_ago:
                send_notification_email(email_info.email,email_info.client, email_info.branch_id, email_info.address, email_info.equipment_type, email_info.replacement_date, "7 days")
                logger.info(f'Replacement notification for {i.equipment_type} - {i.location.branch_id} at {i.location.address}')
                message_to_broadcast = (f'Hello, your {email_info.equipment_type} installed at {email_info.branch_id} - {email_info.address} is due for replacement in 7days time')
                client.messages.create(to=i.location.clients.phone_number,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)

            if timezone.now().date() == day_2_ago:
                send_notification_email(email_info.email,email_info.client, email_info.branch_id, email_info.address, email_info.equipment_type, email_info.replacement_date, "2 days")
                logger.info(f'Replacement notification for {i.equipment_type} - {i.location.branch_id} at {i.location.address}')
                message_to_broadcast = (f'Hello, your {email_info.equipment_type} installed at {email_info.branch_id} - {email_info.address} is due for replacement in 2days time')
                client.messages.create(to=i.location.clients.phone_number,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)

            if timezone.now().date() == i.replacement_date:
                send_notification_email(email_info.email, email_info.client, email_info.branch_id, email_info.address, email_info.equipment_type, email_info.replacement_date, "Today")
                logger.info(f'Replacement notification for {i.equipment_type} - {i.location.branch_id} at {i.location.address}')

                message_to_broadcast = (f'Hello, your {email_info.equipment_type} installed at {email_info.branch_id} - {email_info.address} is due for replacement today')
                client.messages.create(to=i.location.clients.phone_number,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
