from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    is_finished = models.TextField()
    image_url = models.URLField(default="https://cdn.discordapp.com/attachments/1027273502060982372/1027407971828908032/ToDoicon.png")

