from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, ProjectStatsView

urlpatterns = [
    path('',          ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ProjectDetailView.as_view(),     name='project-detail'),
    path('stats/',    ProjectStatsView.as_view(),      name='project-stats'),
]