from pyexpat import model
from tkinter import CASCADE
from xml.etree.ElementTree import Comment
from django.db import models
from django.forms import CharField
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="writer")
    content = models.TextField()
    likey = models.ManyToManyField(User,blank=True,related_name="likey")
    pubdate= models.DateTimeField()

    def __str__(self):
        return self.subject
    def summary(self):
        if len(self.content)>100:
            return f"{self.content[:100]}"
        return self.content
class Reply(models.Model):
    b = models.ForeignKey(Board,on_delete=models.CASCADE)# Board입장에서 참조-Board_set
    replyer = models.ForeignKey(User,on_delete=models.CASCADE)# User입장에서 참조 User-set
    comment = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return f"{self.b}__{self.replyer}"
