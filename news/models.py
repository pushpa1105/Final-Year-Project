from django.db import models

# Create your models here.
from django.db import models
import uuid

# Create your models here.

class information(models.Model):
    n_title = models.CharField(max_length = 50, null = False)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable= False)
    display_images = models.ImageField(null = False, blank = True )
    description = models.TextField(null = True, blank = True)
    n_url=models.URLField(max_length=2000)

    def __str__(self):
        return self.n_title



   