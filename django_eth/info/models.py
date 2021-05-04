from django.db import models

class Rig(models.Model):
    name=models.CharField(max_length=100)
    entry_datetime=models.DateTimeField(auto_now_add=True)
    is_power_on=models.BooleanField()
    gpu_temp=models.IntegerField()
    realtime_hashrate=models.FloatField()
    accepted_hashrate=models.FloatField()
    lifetime_earning=models.FloatField()
    costs=models.IntegerField()

class Pool(models.Model):
    entry_datetime=models.DateTimeField(auto_now_add=True)
    gasprice_rapid = models.IntegerField()
    gasprice_fast = models.IntegerField()
    gasprice_standard = models.IntegerField()
    gasprice_slow=models.IntegerField()

class ETHUSD(models.Model):
    entry_datetime = models.DateTimeField(auto_now_add=True)
    price=models.FloatField()