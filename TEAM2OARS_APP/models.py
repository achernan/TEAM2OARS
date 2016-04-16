from __future__ import unicode_literals

from django.db import models

class Testimonies(models.Model):
    testimonial_id = models.IntegerField(primary_key=True)
    testimonial_date = models.DateField()
    testimonial_content = models.TextField()
    tenant_ss = models.IntegerField(null=False)
