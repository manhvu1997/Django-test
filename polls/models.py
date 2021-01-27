from django.db import models

# Create your models here.
class Question(models.Model):
    questiontext = models.CharField(max_length=200)
    timepublic = models.DateTimeField()

class choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choicetext = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)