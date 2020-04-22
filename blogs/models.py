from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
