from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
# Create your models here.

class Word(models.Model):

    word = models.CharField(primary_key = True, max_length = 250)
    audio_links = ArrayField(models.CharField(max_length = 500), default = list)
    pronounciations = ArrayField(models.CharField(max_length =500), default = list)

    def __str__(self):
        return self.word

class WordDefinition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='defenitions')
    part_of_speech = models.CharField(max_length = 250)
    examples = ArrayField(models.TextField(), default = list)
    synonyms = ArrayField(models.CharField(max_length = 500), default = list)
    priority = models.IntegerField(default=0)
    definitions =  ArrayField(models.TextField())
    def __str__(self):
        return str(self.word.word) + ' - ' + str(self.part_of_speech)  

class Translation(models.Model):
    language = models.CharField(max_length = 250, default = '')
    word = models.ForeignKey(Word, on_delete = models.CASCADE, related_name='translations')
    meaning = models.TextField(default = '')
    local_word = models.CharField(max_length = 1000, default = '')
    utf_encoded = models.CharField(max_length = 1000, default = '')
    def __str__(self):
        return str(self.word.word) + ' - ' + str(self.local_word)  