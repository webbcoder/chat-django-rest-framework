from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Chat room model
class Room(models.Model):
    creator = models.ForeignKey(User, verbose_name="Creator", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Members", related_name="invited_user")
    date = models.DateTimeField("Date creation", auto_now_add=True)

    class Meta:
        verbose_name = "Chat room"
        verbose_name_plural = "Cats rooms"


# Chat model
class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name="Chat room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Post Date", auto_now_add=True)

    class Meta:
        verbose_name = "Chat room"
        verbose_name_plural = "Cats rooms"
