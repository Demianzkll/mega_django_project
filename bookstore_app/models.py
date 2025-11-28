from django.db import models
from datetime import timezone

class TimeAwareModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

# Create your models here.
class Book(TimeAwareModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    
    def save(self, *args, **kwargs):
        self.title = "Blah-blah"
        # self.updated_at = timezone.now()
        # self.created_at = timezone.now()
        return super().save(args, kwargs)
    