from django.db import models
import uuid

# Create your models here.

class plants(models.Model):
    plant_name = models.CharField(max_length = 50, null = False)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable= False)
    display_images = models.ImageField(null = False, blank = True, default = 'default_images' )
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.plant_name


class predict(models.Model):
    images = models.ImageField(null = False, blank = True, default = 'default_images' )
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 50, null = True, blank = True)
    disease = models.CharField(max_length = 50, null = True, blank = True)
    