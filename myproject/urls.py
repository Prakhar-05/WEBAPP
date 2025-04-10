from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# JWT Authentication Views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Swagger Documentation Setup
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger Schema Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Detailed API Documentation for Admin & User APIs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Default root: serve user portal HTML
    path('', TemplateView.as_view(template_name='user_portal.html'), name='home'),

    # Django Admin
    path('admin/', admin.site.urls),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Endpoints
    path('api/admin_panel/', include('admin_panel.urls')),
    path('api/user_app/', include('user_app.urls')),

    # Swagger & Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Only serve media in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
