from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# ✅ Serve the user portal HTML page
class UserPortalView(TemplateView):
    template_name = 'user_portal.html'

# ✅ Signup endpoint
@api_view(['POST'])
def signup_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

# ✅ Placeholder: View profile
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
        })

# ✅ Placeholder: Update email
class UpdateUserEmailView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        new_email = request.data.get('email')
        request.user.email = new_email
        request.user.save()
        return Response({'message': 'Email updated successfully'})

# ✅ Placeholder: List apps
class AndroidAppUserListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'apps': []})  # Empty list for now

# ✅ Placeholder: Submit tasks
class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        return Response({'message': 'Task created (dummy response)'})
