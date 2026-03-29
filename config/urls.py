from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import TemplateView

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
    path('',                 TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/',           admin.site.urls),
    path('api/v1/projects/', include('projects.urls')),
]