from django.urls import path
from .views import (
    UserPortalView,              # ✅ Main user portal page
    UserProfileView,             # ✅ Profile view
    UpdateUserEmailView,         # ✅ Profile update
    AndroidAppUserListView,      # ✅ List apps
    TaskCreateView,              # ✅ Submit tasks
    signup_user,                 # ✅ Signup API
)

urlpatterns = [
    # Serve the main user portal HTML page.
    path('', UserPortalView.as_view(), name='user-portal'),

    # Signup endpoint.
    path('signup/', signup_user, name='signup'),

    # Profile endpoints.
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UpdateUserEmailView.as_view(), name='user-profile-update'),

    # App listing for users.
    path('apps/', AndroidAppUserListView.as_view(), name='user-app-list'),

    # Task submission.
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
]
