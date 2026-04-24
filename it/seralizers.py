from rest_framework import serializers
from .models import Project, BugReport, Laptop


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class BugReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugReport
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'