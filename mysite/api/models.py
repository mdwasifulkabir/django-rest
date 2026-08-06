from django.db import models

# Create your models here.
class Quote(models.Model):
  quote = models.TextField()
  source = models.Charfield()

  def __str__(self):
    return self.quote