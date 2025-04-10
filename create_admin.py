from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

User = get_user_model()

def create_default_admin():
    admin_username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
    admin_password = os.getenv('DJANGO_ADMIN_PASSWORD', 'adminpass')
    admin_email = os.getenv('DJANGO_ADMIN_EMAIL', 'admin@example.com')

    if not User.objects.filter(username=admin_username).exists():
        print("Creating default admin...")
        User.objects.create_superuser(username=admin_username, password=admin_password, email=admin_email)
    else:
        print("Default admin already exists.")
