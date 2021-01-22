from django.test import TestCase
from .models import AD
from django.utils import timezone
from .forms import CustomUserCreationForm
from django.core import mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        ad.send_mail('Subject here', 'Here is the message.',
            'rababalesead12@gmail.com', ['rababkhalifamohammed@gmail.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


