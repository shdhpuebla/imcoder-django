from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField

STATUS = ((1,'Disponible'),
        (2,'No Disponible'),
        (3, 'Freelance'),
)

class Coder(models.Model):
    user = models.OneToOneField(User)
    languages = TagField()
    status = models.CharField(max_length=20, choices=STATUS)
    recommended = models.ManyToManyField(User, related_name='r+')
    friends = models.ManyToManyField(User, related_name='f+')

