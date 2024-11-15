
import json
from django.http import JsonResponse
from .services import register_name, resolve_name
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_name_view(request):
    if request.method == "POST":
        try:
            # Cargar los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)
            
            # Obtener los datos del JSON (con valores por defecto si no existen)
            namespace = data.get("namespace", "global")
            resource_type = data.get("resource_type")
            metadata = data.get("metadata", "{}")
            
            # Verificar que 'resource_type' esté presente
            if not resource_type:
                return JsonResponse({"error": "'resource_type' is required."}, status=400)
            
            # Registrar el recurso
            resource = register_name(namespace, resource_type, metadata)
            
            # Responder con el recurso registrado
            return JsonResponse({"name": str(resource)}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

def resolve_name_view(request, namespace, resource_type, unique_id):
    resource = resolve_name(namespace, resource_type, unique_id)
    if resource:
        return JsonResponse({"name": str(resource), "metadata": resource.metadata})
    return JsonResponse({"error": "Resource not found"}, status=404)