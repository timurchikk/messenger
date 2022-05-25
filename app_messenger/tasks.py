from datetime import datetime

from celery import shared_task

@shared_task
def add_sheduled_messages():
    from .models import Message, SheduledMessage
    date_and_time = datetime.now()
    date = date_and_time.date()
    hours = date_and_time.hour
    minutes = date_and_time.minute
    sheduled_messages = SheduledMessage.objects.filter(s_date_time__date=date, s_date_time__hour=hours, s_date_time__minute=minutes)
    if sheduled_messages.exists():
        for i in sheduled_messages:
            message = Message.objects.create(
                owner = i.s_owner,
                recepient = i.s_recepient,
                message = i.s_message,
                file_message = i.s_file_message,
            )
            message.save()
            i.delete()
        return 'Sheduled messages sucessful added'
    else:
        return 'Dont have a sheduled messages'