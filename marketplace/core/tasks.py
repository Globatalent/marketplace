# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail

from marketplace.taskapp.celery import app


@app.task
def send_mail_task(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None,
                    auth_password=None, connection=None, html_message=None):
    send_mail(subject, message, from_email, recipient_list, fail_silently=fail_silently, auth_user=auth_user,
              auth_password=auth_password, connection=connection, html_message=html_message)
