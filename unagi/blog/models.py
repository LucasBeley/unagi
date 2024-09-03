from django.contrib import admin
from django.db import models


class Post(models.Model):
    title = models.CharField("title", max_length=255)
    cover_image_url = models.URLField("cover image url", max_length=255, null=True, default=None, blank=True)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)
    posted_at = models.DateTimeField("posted at", null=True, default=None, blank=True)
    hidden_at = models.DateTimeField("hidden at", null=True, default=None, blank=True)
    content = models.TextField("content")

    @admin.display(
        boolean=True,
        ordering="posted_ad",
        description="Online?",
    )
    def is_online(self):
        return self.posted_at is not None and self.hidden_at is None

    def __str__(self):
        return self.title
