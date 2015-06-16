from django.db import models
class Document(models.Model):
    document_title = models.CharField(max_length=100)
    document_desc = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='media')