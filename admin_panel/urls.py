from django.urls import path
from .views import AdminDashboardView, AndroidAppListView, AndroidAppCreateView

urlpatterns = [
    # Serves the admin dashboard HTML template
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    
    # API endpoint to list all Android apps for admin
    path('android-apps/', AndroidAppListView.as_view(), name='android_apps_list'),
    
    # API endpoint to create a new Android app (admin only)
    path('android-apps/create/', AndroidAppCreateView.as_view(), name='android_app_create'),
]
