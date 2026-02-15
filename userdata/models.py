from django.db import models


class UserInpSol(models.Model):
    csrftoken = models.CharField(default=1)
    inp = models.CharField()
    sol = models.CharField()
