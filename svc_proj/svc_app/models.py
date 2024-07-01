from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import JSONField
from jsonschema import validate, ValidationError as JSONSchemaValidationError

# Define the meta-schema for key_schema validation
meta_schema = {
   "required": ["type", "properties"]
}

class AnnotationKey(models.Model):
    key_name = models.CharField(max_length=255)
    key_schema = JSONField()



class AnnotationDelegateService(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    annotation_keys = models.ManyToManyField(AnnotationKey, related_name='services')
    depends_on_keys = models.ManyToManyField(AnnotationKey, related_name='dependent_services', blank=True)
    max_retries = models.PositiveIntegerField(default=3)
    retry_delay = models.PositiveIntegerField(default=5)
    timeout = models.PositiveIntegerField(default=15)

    def __str__(self):
        return self.name
