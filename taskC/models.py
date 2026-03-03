from django.db import models

class UserTasks(models.Model):
    csrftoken = models.CharField(default=1)
    inp = models.CharField()
    sol = models.CharField()

    def __str__(self):
        return str(self.inp)