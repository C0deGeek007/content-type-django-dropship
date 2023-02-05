from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class ProjectModel(models.Model):
    description = models.TextField()
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comments = GenericRelation("Comment")

class Comment(models.Model):
    body = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.body

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]