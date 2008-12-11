from django.db import models

class Smiley(models.Model):
    pattern = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='smileys')
    is_regex = models.BooleanField(blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    def __unicode__(self):
        return self.description or self.pattern

    class Meta:
        ordering = ['description', 'pattern']