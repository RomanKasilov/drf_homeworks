import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def send_test_email(cls):
        cls.__send_email(to='kasiakasilov@gmail.com', template_name='test.html', subject='Test Email', context={})

    @classmethod
    def register_email(cls, user: User):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email(
            to=user.email,
            template_name='register.html',
            context={'name': user.profile.name, 'url': url},
            subject='Register email'
        )