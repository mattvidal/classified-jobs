from django.db import models
from uuid import uuid4
from .validator import validate_id_document_length 

# Create your models here.

class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length = 200, null=False )
    birth_date = models.DateField(null=False)
    id_document = models.CharField(max_length=14, validators=[validate_id_document_length])
    description = models.CharField(max_length=1000, null=False)

    create_at = models.DateField(auto_now_add=True)

class JobVacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length = 100,  null=False)
    create_at = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000, null=False)


class Employer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length = 200, null=False )
    url = models.URLField(null=False)
    create_at = models.DateField(auto_now_add=True)
    

