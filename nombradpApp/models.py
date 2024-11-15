from django.db import models
import uuid

class ResourceName(models.Model):
    namespace = models.CharField(max_length=100, default="global")
    resource_type = models.CharField(max_length=100)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    metadata = models.JSONField(default=dict)  # Almacena datos adicionales
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.namespace}:{self.resource_type}:{self.unique_id}"