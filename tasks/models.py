from django.db import models

class Task(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

