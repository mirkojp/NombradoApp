from .models import ResourceName

def register_name(namespace, resource_type, metadata=None):
    resource = ResourceName.objects.create(
        namespace=namespace,
        resource_type=resource_type,
        metadata=metadata or {}
    )
    return resource

def resolve_name(namespace, resource_type, unique_id):
    try:
        return ResourceName.objects.get(
            namespace=namespace,
            resource_type=resource_type,
            unique_id=unique_id
        )
    except ResourceName.DoesNotExist:
        return None
