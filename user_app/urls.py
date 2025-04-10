from django.urls import path
from .views import (
    UserPortalView, AndroidAppUserListView,
    TaskCreateView, UserProfileView, UpdateProfileView
)

urlpatterns = [
    path('', UserPortalView.as_view(), name='user-portal'),
    path('apps/', AndroidAppUserListView.as_view(), name='user-app-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='user-profile-update'),  # ✅ Add this
]
