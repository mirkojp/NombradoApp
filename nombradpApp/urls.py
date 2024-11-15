from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_name_view, name="register_name"),
    path("resolve/<str:namespace>/<str:resource_type>/<uuid:unique_id>/", views.resolve_name_view, name="resolve_name"),
]