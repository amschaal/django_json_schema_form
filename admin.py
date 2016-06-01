from django.contrib import admin
from models import Questionnaire


# class QuestionnaireAdmin(admin.ModelAdmin):
#     add_form_template = 'admin/django_jsf/add_form.html'
#     change_form_template = 'admin/django_jsf/change_form.html'
admin.site.register(Questionnaire)

