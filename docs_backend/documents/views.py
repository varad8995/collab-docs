from rest_framework import viewsets, permissions
from .models import Document
from .serializers import DocumentSerializer
from rest_framework import generics
from .models import Collaborator
from .serializers import CollaboratorSerializer
from rest_framework.permissions import IsAuthenticated

class IsOwnerOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        if request.user in obj.collaborators.all():
            return True
        return False

from rest_framework.exceptions import NotAuthenticated

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Check if the user is authenticated
        if not self.request.user.is_authenticated:
            raise NotAuthenticated("You must be logged in to view documents.")
        
        # Return documents where the user is the owner or a collaborator
        return Document.objects.filter(owner=self.request.user) | Document.objects.filter(collaborators=self.request.user)

    def perform_create(self, serializer):
        # Ensure the owner is set to the current authenticated user
        serializer.save(owner=self.request.user)

class CollaboratorCreateView(generics.CreateAPIView):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer