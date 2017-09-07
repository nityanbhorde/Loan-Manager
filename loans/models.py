from django.db import models

class Loan(models.Model):
    name = models.CharField(max_length = 200)
    money = models.IntegerField()
    def absolute(self):
        return abs(self.money)