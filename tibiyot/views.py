from rest_framework.viewsets import ModelViewSet
from .models import Doctor, Patient, Appointment, Medicine
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, MedicineSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class MedicineViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer