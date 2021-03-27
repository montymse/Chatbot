from django.db import models


# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return "/chat/%s/" % self.room_name