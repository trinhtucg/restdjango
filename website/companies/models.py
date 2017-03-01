from django.db import models

# Create your models here.


class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    class Meta:
        db_table = 'tb_stock'

    def __str__(self):
        return self.ticker
