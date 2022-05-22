import uuid
from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    class Meta:
        verbose_name_plural = 'Words'

    def __str__(self):
        return str(self.word)

class WordMeaning(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    word = models.ForeignKey('dictionary.Words', on_delete=models.CASCADE)
    meaning = models.CharField(max_length=100)
    priority = models.IntegerField()

    def __str__(self):
        return str(self.word)