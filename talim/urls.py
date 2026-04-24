from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet,StudentViewSet,CourseViewSet,SubjectViewSet,GradeViewSet,LibraryCardViewSet

router = DefaultRouter()
router.register(r'group', GroupViewSet)
router.register(r'student', StudentViewSet)
router.register(r'course', CourseViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'librarycard', LibraryCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]