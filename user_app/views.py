from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from admin_panel.models import AndroidApp
from admin_panel.serializers import AndroidAppSerializer
from .models import Task
from .serializers import TaskSerializer, UserSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

# This view serves the user portal HTML page.
class UserPortalView(TemplateView):
    template_name = 'user_portal.html'  # Path to your HTML template

# API view to list all Android apps for users.
class AndroidAppUserListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        apps = AndroidApp.objects.all()
        serializer = AndroidAppSerializer(apps, many=True)
        return Response(serializer.data)

# API view for users to create a new task (upload a screenshot).
class TaskCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # Save the task and update user stats
            task = serializer.save(user=request.user)
            user = request.user
            user.tasks_completed += 1
            # Ensure task.app.points exists and is numeric
            user.points_earned += task.app.points  
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view for retrieving the logged-in user's profile.
class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

# API view for updating the logged-in user's email.
class UpdateUserEmailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.email = email
        request.user.save()
        return Response({"email": request.user.email}, status=status.HTTP_200_OK)
