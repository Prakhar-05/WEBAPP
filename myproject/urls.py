from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# JWT Authentication Views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

# Swagger Documentation Setup
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Custom Token view to add error logging.
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            print("JWT Token Error:", e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    # Default route serves the user portal HTML page
    path('', TemplateView.as_view(template_name='user_portal.html'), name='home'),

    # Django Admin site
    path('admin/', admin.site.urls),

    # JWT Auth endpoints using the custom view.
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Endpoints for custom apps
    path('api/admin_panel/', include('admin_panel.urls')),
    path('api/user_app/', include('user_app.urls')),

    # Swagger & Redoc documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
