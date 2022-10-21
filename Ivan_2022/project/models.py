from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title
