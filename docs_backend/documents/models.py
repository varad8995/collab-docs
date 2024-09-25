from django.contrib.auth.models import User
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Storing the document content as plain text or JSON for rich text.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    collaborators = models.ManyToManyField(User, related_name='shared_documents', through='Collaborator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Collaborator(models.Model):
    ROLE_CHOICES = [
        ('edit', 'Can Edit'),
        ('view', 'Can View'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)
    added_at = models.DateTimeField(auto_now_add=True)
