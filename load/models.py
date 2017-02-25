from django.db import models

TITLE_CHOICES = (
    ('ND', 'Not Done'),
    ('D', 'Done'),
)

class Complaint(models.Model):
    num = models.IntegerField(max_length=10,default=1)
    comp = models.CharField(max_length=100)
    status = models.CharField(max_length=10,choices=TITLE_CHOICES)
    def __str__(self):
        return self.comp+" - "+self.status