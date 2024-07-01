from django import forms
import json
from django.conf import settings

class DynamicJSONFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        # Remove the 'encoder' argument if it's present for SQLite
        if settings.DATABASES['default']['ENGINE'] != 'django.db.backends.postgresql':
            kwargs.pop('encoder', None)  
            kwargs.pop('decoder', None)  

        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        if value:
            try:
                parsed = json.loads(value)
                return json.dumps(parsed, indent=4)
            except json.JSONDecodeError:
                pass  # Handle invalid JSON gracefully
        return value
