from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, CollaboratorCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Set up the router for the DocumentViewSet
router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')  # Registering DocumentViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh
    path('collaborators/', CollaboratorCreateView.as_view(), name='add-collaborator'),  # Add collaborator endpoint
]
