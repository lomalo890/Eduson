from django.db import models
from django.contrib.admin import display

# Create your models here.
class Play(models.Model):
    title = models.CharField(max_length=255)
    annotations = models.TextField()


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True) # maybe null

    
class Show(models.Model):
    start_at = models.DateTimeField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor) # много показов могут ссылаться на одного актёра

    @display
    def play_name(self):
        return self.play.title

