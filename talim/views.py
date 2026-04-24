from rest_framework.viewsets import ModelViewSet
from .models import Group, Student, Course, Subject, Grade, LibraryCard
from .serializers import GroupSerializer,StudentSerializer,CourseSerializer,SubjectSerializer,GradeSerializer,LibraryCardSerializer



class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class LibraryCardViewSet(ModelViewSet):
    queryset = LibraryCard.objects.all()
    serializer_class = LibraryCardSerializer