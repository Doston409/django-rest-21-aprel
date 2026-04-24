from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet, MedicineViewSet

router = DefaultRouter()
router.register(r'doctor', DoctorViewSet)
router.register(r'patient', PatientViewSet)
router.register(r'appointment', AppointmentViewSet)
router.register(r'medicine', MedicineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]