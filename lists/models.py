from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey('List', default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text


class List(models.Model):

    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])
