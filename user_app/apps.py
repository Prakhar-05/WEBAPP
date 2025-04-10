from django.apps import AppConfig

class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_app'

    def ready(self):
        from django.db.utils import OperationalError
        try:
            from myproject.create_admin import create_default_admin
            create_default_admin()
        except OperationalError:
            pass  # Database might not be ready yet
        except Exception as e:
            print("Error creating default admin:", e)

