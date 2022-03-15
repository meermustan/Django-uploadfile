from django.db import models

class Beast(models.Model):
    MOM_CLASSIFICATIONS = [
    ('XXXXX', 'Known Wizard  Killer'),
    ('XXXX', 'Dangerous'),
    ('XXX', 'Competent wizard should cope'),
    ('XX', 'Harmless'),
    ('X', 'Boring'),
    ]
    name = models.CharField(max_length=60)
    mom_classification = models.CharField(max_length=5, choices=MOM_CLASSIFICATIONS)
    description = models.TextField()
    media = models.FileField(upload_to="media", null=True, blank=True)