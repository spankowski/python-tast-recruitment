from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Debt(models.Model):
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creditor')
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debtor')
    debt = models.IntegerField()

    def __str__(self):
        return str(self.debt)+"--"+str(self.debtor)