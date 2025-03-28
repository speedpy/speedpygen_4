from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
class User(models.Model):
    username = models.CharField(blank=False, null=False, unique=True)
    email = models.CharField(blank=False, null=False, unique=True)
    password = models.CharField(blank=False, null=False)
    def __str__(self):
        return str(self.id)

class Image(models.Model):
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_images")
    original_image = models.ImageField(blank=False, null=False, upload_to="original_image_images/")
    ghibli_styled_image = models.ImageField(blank=True, null=True, upload_to="ghibli_styled_image_images/")
    upload_date = models.DateTimeField(default=timezone.now, blank=False, null=False)
    def __str__(self):
        return str(self.id)

class ImageCollection(models.Model):
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_imagecollections")
    name = models.CharField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    images = models.ManyToManyField(blank=True, null=True, to="mainapp.Image", related_name="images_imagecollections")
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    def __str__(self):
        return str(self.name)

class GhibliStyle(models.Model):
    name = models.CharField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.name)

class StyledImageJob(models.Model):
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_styledimagejobs")
    image = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Image", related_name="image_styledimagejobs")
    style = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.GhibliStyle", related_name="style_styledimagejobs")
    status = models.CharField(default='pending', blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
