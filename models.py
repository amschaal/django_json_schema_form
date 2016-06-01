from __future__ import unicode_literals
from jsonfield import JSONField
from django.db import models
import collections

class Questionnaire(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    schema = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
    form = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
    
class Survey(models.Model):
    id = models.UUIDField(primary_key=True)
    questionnaire = models.ForeignKey(Questionnaire)
    created = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    id = models.UUIDField(primary_key=True)
    survey = models.ForeignKey(Survey, related_name='responses')
    answers = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})

