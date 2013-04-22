from django.db import models
from django.contrib.auth.models import User

class Favorites(models.Model):
    user = models.ForeignKey(User)
    program_id = models.IntegerField()
    created_at = models.DateTimeField('date created at')
    updated_at = models.DateTimeField('date updated at')
    def __unicode__(self):
        return "user_id: %d and program_id: %d" %(self.user_id, self.program_id)
    
