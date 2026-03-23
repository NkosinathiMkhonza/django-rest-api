from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({
        "message": "Welcome to Nkosinathi's Django REST API",
        "version": "v1",
        "endpoints": {
            "projects": "/api/v1/projects/",
            "project_detail": "/api/v1/projects/<id>/",
            "project_stats": "/api/v1/projects/stats/",
        },
        "github": "https://github.com/NkosinathiMkhonza/django-rest-api",
        "author": "Nkosinathi Mkhonza"
    })


urlpatterns = [
    path('',                 api_root,              name='api-root'),
    path('admin/',           admin.site.urls),
    path('api/v1/projects/', include('projects.urls')),
]