from django.db import models
from django.conf import settings

""


class Intervention(models.Model):
    
    title_intervention = models.CharField(
        max_length=300, help_text='Enter the interventions title')
    
    description = models.TextField(
        max_length=300, help_text='Enter the instervention description intervention')
    
    adress_intervention = models.TextField(
        max_length=300, help_text='Enter the instervention description')
    
    date_intervention = models.TextField(help_text='Enter the instervention date')
    

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.command[:20]
