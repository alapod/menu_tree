from django.db import models


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)
