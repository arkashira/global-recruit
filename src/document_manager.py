import json
from dataclasses import dataclass
from typing import Dict, List
import hashlib
import hmac
import os

@dataclass
class Document:
    id: str
    type: str
    expiry_date: str
    content: str

class DocumentManager:
    def __init__(self):
        self.documents = {}
        self.metadata = {}
        self.key = os.urandom(32)  # Generate a fixed key

    def upload_document(self, document: Document):
        encrypted_content = self._encrypt_content(document.content)
        self.documents[document.id] = encrypted_content
        self.metadata[document.id] = {
            'type': document.type,
            'expiry_date': document.expiry_date
        }

    def _encrypt_content(self, content: str):
        return hmac.new(self.key, content.encode(), hashlib.sha256).hexdigest()

    def search_documents(self, document_type: str):
        return [id for id, metadata in self.metadata.items() if metadata['type'] == document_type]

    def get_document(self, document_id: str):
        if document_id in self.documents:
            return self.documents[document_id]
        else:
            raise ValueError("Document not found")

    def update_document(self, document_id: str, new_document: Document):
        if document_id in self.documents:
            self.upload_document(new_document)
        else:
            raise ValueError("Document not found")

    def delete_document(self, document_id: str):
        if document_id in self.documents:
            del self.documents[document_id]
            del self.metadata[document_id]
        else:
            raise ValueError("Document not found")
