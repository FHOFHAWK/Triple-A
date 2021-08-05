from django.db import models


class LessonVideo(models.Model):
    video_hash = models.CharField(max_length=256)
