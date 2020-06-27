from django.db import models
from django.urls import reverse
# Create your models here.


class Student(models.Model):
    GRADE_CHOICES=(('a','A'),('b','B'),('c','C'),('d','D'))
    roll_number=models.IntegerField('Roll Number')
    name=models.CharField('Name',max_length=56)
    marks=models.IntegerField('Marks')
    grade=models.CharField('Grade',choices=GRADE_CHOICES,default='b',max_length=90)
    address=models.TextField(verbose_name='Address')

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        return reverse('detail_view',kwargs={'pk':self.pk})
