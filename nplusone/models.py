from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)


class UploadDay(models.Model):
    day = models.CharField(max_length=5, unique=True)


class Writer(models.Model):
    name = models.CharField(max_length=10, unique=True)


class WebToon(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    writer = models.OneToOneField(Writer, on_delete=models.CASCADE)
    upload_date = models.ForeignKey(UploadDay, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
