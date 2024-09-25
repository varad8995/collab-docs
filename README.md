# Collab Docs - Collaborative Document Sharing Platform

**Collab Docs** is a document-sharing platform inspired by Google Docs. It allows multiple users to collaborate on documents in real-time, with support for role-based permissions (view or edit). Built using Django and Django REST Framework, it provides a robust backend API for managing documents, users, and collaborations, with optional real-time features powered by WebSockets (using Django Channels).

## Features

- User Authentication (JWT-based)
- Create, edit, and delete documents
- Share documents with collaborators (view/edit permissions)
- Real-time collaboration (via WebSockets)
- Document versioning and change tracking
- Fine-grained access control (Owner/Collaborator)
- RESTful API for easy integration with frontend applications

## Project Structure

