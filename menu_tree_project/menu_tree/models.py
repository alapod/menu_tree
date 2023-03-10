from django.db import models


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.slug
