from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import AndroidApp
from .serializers import AndroidAppSerializer
from django.views.generic import TemplateView

# This view serves the admin dashboard HTML page.
class AdminDashboardView(TemplateView):
    template_name = 'admin_dashboard.html'  # Adjust path if nested

# API view to create a new Android app (admin only).
class AndroidAppCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer

# API view to list all Android apps (admin only).
class AndroidAppListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
