from rest_framework.viewsets import ModelViewSet
from .models import Project, BugReport, Laptop
from .serializers import ProjectSerializer, BugReportSerializer, LaptopSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class BugReportViewSet(ModelViewSet):
    queryset = BugReport.objects.all()
    serializer_class = BugReportSerializer


class LaptopViewSet(ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer