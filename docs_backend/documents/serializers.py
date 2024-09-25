from rest_framework import serializers
from .models import Document, Collaborator

class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    collaborators = serializers.StringRelatedField(many=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'owner', 'collaborators', 'created_at', 'updated_at']

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ['user', 'document', 'role', 'added_at']
