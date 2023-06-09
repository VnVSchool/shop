from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Slide(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/")
    is_first_slide = models.BooleanField(default=False)

    def __str__(self):
        return self.title