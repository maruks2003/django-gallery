from django.db import models
import time

class Tag(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=200)

def get_filename(instance, filename):
    ext = filename.split(".")[-1]
    return "images/" + str(int(time.time()*10)) + "." + ext

class ImagePost(models.Model):
    def __str__(self) -> str:
        return self.image.name

    image = models.ImageField(upload_to=get_filename)
    tags = models.ManyToManyField(Tag, blank=True)

