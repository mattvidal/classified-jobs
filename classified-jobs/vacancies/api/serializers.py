from rest_framework import serializers
from vacancies import models   

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidate
        fields = '__all__'

class JobVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobVacancy
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = '__all__'