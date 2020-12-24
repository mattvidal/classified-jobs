from rest_framework import viewsets
from vacancies.api import serializers
from vacancies import models

class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CandidateSerializer
    queryset = models.Candidate.objects.all()

class JobVacancyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobVacancySerializer
    queryset = models.JobVacancy.objects.all()

class EmployerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployerSerializer
    queryset = models.Employer.objects.all()    