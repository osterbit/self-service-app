from django.contrib import admin
from .models import AnnotationKey, AnnotationDelegateService
# from django_jsonform.widgets import JSONFormWidget
from django.db import models
from django_ace import AceWidget
from .forms import DynamicJSONFormField





@admin.register(AnnotationKey)
class AnnotationKeyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'form_class': DynamicJSONFormField}, 
    }

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'key_schema':
            field.widget = AceWidget(mode='json', theme='twilight') 
        return field

@admin.register(AnnotationDelegateService)
class AnnotationDelegateServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('annotation_keys', 'depends_on_keys')
