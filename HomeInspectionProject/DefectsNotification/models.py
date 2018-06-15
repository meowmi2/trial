from django.db import models

# Create your models here.

class Address(models.Model):
    block = models.IntegerField(default=0, verbose_name='Block')
    unit = models.IntegerField(default=0)
    level = models.IntegerField(default=0, null=False)
    street = models.CharField(max_length=128)

    def __str__(self):
        return self.block +''+ self.unit+ '' + self.level + ''+self.street

    class Meta:
        verbose_name_plural = "Address"


class History(models.Model):
    creation_date = models.DateField()
    completion_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "History"

    def __str__(self):
        return str(self.creation_date)
