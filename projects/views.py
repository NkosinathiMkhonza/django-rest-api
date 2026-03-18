from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset           = Project.objects.all()
    serializer_class   = ProjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Project created successfully.", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Project.objects.all()
    serializer_class = ProjectSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Project updated successfully.", "data": serializer.data}
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Project deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )


class ProjectStatsView(APIView):
    def get(self, request):
        total     = Project.objects.count()
        active    = Project.objects.filter(status='active').count()
        completed = Project.objects.filter(status='completed').count()
        on_hold   = Project.objects.filter(status='on_hold').count()
        return Response({
            "total":     total,
            "active":    active,
            "completed": completed,
            "on_hold":   on_hold,
        })