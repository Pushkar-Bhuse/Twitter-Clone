from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import validate_content


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING)
    content = models.CharField(max_length = 140, validators = [validate_content])
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={'pk': self.pk})


    # def clean(self,*args,**kwargs):
    #     if self.content == '':
    #         raise ValidationError("The content cannot be empty")
    #     return self.content