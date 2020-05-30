from django.db import models
from datetime import datetime

# Create your models here.
class Task_List(models.Model):

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'

    name = models.CharField(max_length=254, default='')
    TYPECHOICES = (
        ('Normal', 'Normal'),
        ('Group', 'Group')
    )
    type = models.CharField(max_length=254, choices=TYPECHOICES, default='')
    parent_list = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    list = models.ForeignKey(Task_List, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='', blank=True)
    due_date = models.DateField(default=datetime.now)
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    importance = models.CharField(max_length=25, choices=YESNOCHOICES)
    completed = models.CharField(max_length=25, choices=YESNOCHOICES, default='No')
    assigned_to = models.IntegerField()

    def __str__(self):
        return self.name