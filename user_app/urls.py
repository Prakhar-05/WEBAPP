from django.urls import path
from .views import (
    UserPortalView,
    UserProfileView,
    UpdateUserEmailView,
    AndroidAppUserListView,
    TaskCreateView,
)

urlpatterns = [
    # Serve the main user portal HTML page.
    path('', UserPortalView.as_view(), name='user-portal'),

    # Profile endpoints.
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UpdateUserEmailView.as_view(), name='user-profile-update'),

    # App listing for users.
    path('apps/', AndroidAppUserListView.as_view(), name='user-app-list'),

    # Task submission.
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
]
