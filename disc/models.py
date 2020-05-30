from django.db import models

# Create your models here.


class MediaType(models.Model):
    """
    Disc type eg: VCD, MP3, AUDIO, MP5, DVD
    """
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Content(models.Model):
    """
    Disc content like movie, data, educational, audio, video, 
    """
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class DiscModel(models.Model):
    media_type = models.ForeignKey(MediaType, on_delete=models.DO_NOTHING)
    content = models.ForeignKey(Content, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
