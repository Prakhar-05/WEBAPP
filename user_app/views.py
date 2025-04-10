from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from admin_panel.models import AndroidApp
from admin_panel.serializers import AndroidAppSerializer
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

# This view serves the user portal HTML page.
class UserPortalView(TemplateView):
    template_name = 'user_portal.html'  # Adjust path if nested

# API view to list all Android apps for users.
class AndroidAppUserListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer

# API view for users to create a new task (upload a screenshot).
class TaskCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        user = self.request.user
        user.tasks_completed += 1
        user.points_earned += task.app.points  # Make sure task.app.points exists
        user.save()

# API view for retrieving the logged-in user's profile.
class UserProfileView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# API view for updating the logged-in user's profile.
class UpdateProfileView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user