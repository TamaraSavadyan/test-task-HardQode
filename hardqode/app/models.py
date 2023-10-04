from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.IntegerField()

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    view_time_seconds = models.IntegerField(default=0)

    def mark_as_viewed(self):
        if self.view_time_seconds >= 0.8 * self.lesson.duration_seconds:
            self.viewed = True
        else:
            self.viewed = False
