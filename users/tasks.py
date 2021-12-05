from celery import shared_task
from celery.utils.log import get_task_logger

from .emails import send_registration_email

logger = get_task_logger(__name__)


@shared_task(name="send_registration_email_task")
def send_registration_email_task(email, password, first_name):
    logger.info("Sent registration email")
    return send_registration_email(email, password, first_name)

