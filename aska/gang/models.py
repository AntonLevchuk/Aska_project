from distutils.command.upload import upload
from msilib.schema import tables
from tabnanny import verbose
from django.db import models

class Member(models.Model):
    """ Gang member's class """
    photo = models.ImageField(upload_to='gang/static/img/members')
    name = models.CharField(max_length=60)
    yt_link = models.CharField(max_length=150)
    ins_link = models.CharField(max_length=150)
    ds_tag = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class Application(models.Model):
    """ Application form class """
    nickname = models.CharField(max_length=20)
    ds_name = models.CharField(max_length=40)
    edit_link = models.CharField(max_length=150)
    other_links = models.CharField(max_length=150)
    result = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nickname, self.ds_name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
