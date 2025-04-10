from django.urls import path
from . import views

urlpatterns = [
    # Optional: serve user_portal.html from this app directly if needed
    path('', views.UserPortalView.as_view(), name='user-portal'),

    # User Profile
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', views.UpdateProfileView.as_view(), name='user-profile-update'),

    # Apps list
    path('apps/', views.AndroidAppListView.as_view(), name='app-list'),

    # Task submission
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
]
