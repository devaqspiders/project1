from django.db import models

class Task(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=250)
    t_desc = models.TextField(null=False,default='')
    priority = models.CharField(max_length=250,null=False,choices=[('HIGH','high'),('LOW','low'),('AVERAGE','average')])

    def __str__(self):
        return self.t_name