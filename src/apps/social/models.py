import datetime
import decimal

from django.db import models


ARTICLE_TYPE = (
    ("", "Select Type"),
    ("private", "Private"),
    ("public", "Public"),
)


class Article(models.Model):

    """
    Article Base Class
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    article_type = models.CharField(
        max_length=255,
        choices=ARTICLE_TYPE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
        Comment Base Class
    """

    article = models.ForeignKey(
        Article,
        related_name="comments",
        null=True,
        blank=True
        )
    commenter = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.commenter
