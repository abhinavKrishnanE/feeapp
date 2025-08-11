from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import requests
from datetime import datetime

from feeapp.models import FeeNotification


@shared_task
def send_email():

    today = timezone.now().date()
    #print(today)
    upcoming_due_students = []

    notifications = FeeNotification.objects.select_related('student_batch_fee_details').all()
    response = requests.post('http://127.0.0.1:8000/testapp/studentbatchdetailsapi/')

    for notification in notifications:
        details = notification.student_batch_fee_details
        fee_structure = details.fee_structure
        if fee_structure.due_type == 'fixed':
            due_date = timezone.datetime(timezone.now().year, timezone.now().month, fee_structure.fixed_due_date).date()
        else:
            for student in response.json():
                if int(student['id']) == int(details.student_id):
                    due_date = student['joined_date']
                    break
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
            due_date = timezone.datetime(timezone.now().year, timezone.now().month, due_date.day).date()
            
        notify_date = due_date - timedelta(days=notification.notify_before_days)
        #print("n", notify_date)
        if today >= notify_date:
            upcoming_due_students.append(notification.student_batch_fee_details.student_id)
    #print(upcoming_due_students)
    response = requests.post(
            'http://127.0.0.1:8000/testapp/studentdetailsapi/',
            json={'student_ids': upcoming_due_students}
        )
    emails = []
    for student in response.json():
        emails.append(student['email'])
    print(emails)
    if emails:
        subject = "Hii"
        message = 'your fee is due'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = emails

        send_mail(subject, message, from_email, recipient_list)