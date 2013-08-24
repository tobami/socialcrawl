from django.db import models
from django.core.exceptions import ValidationError


class Profile(models.Model):
    SOCIAL_NETWORKS = (
        ('T', 'Twitter'),
        ('F', 'Facebook'),
    )
    username = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    popularity = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    network = models.CharField(max_length=1,
                               blank=False,
                               choices=SOCIAL_NETWORKS)

    def clean(self):
        if not self.username:
            raise ValidationError('No username defined')
        elif not self.network:
            raise ValidationError('No network defined')

    def save(self, *args, **kwargs):
        self.clean()
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('username', 'network')
