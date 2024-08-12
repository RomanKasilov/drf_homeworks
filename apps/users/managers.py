from django.contrib.auth.models import UserManager as Manager


class UserManager(Manager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('email required')
        if not password:
            raise ValueError('password required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields['is_active']:
            raise ValueError('is_active should be True')
        if extra_fields['is_staff']:
            raise ValueError('is_staff should be True')
        if extra_fields['is_superuser']:
            raise ValueError('is_superuser should be True')
        user = self.create_user(email, password, **extra_fields)
        return user
