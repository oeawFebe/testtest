from django.shortcuts import render
from .models import Rig,Pool,ETHUSD
def index(request):
    rigs=Rig.objects.all()
    pool=Pool.objects.last()
    ethusd=ETHUSD.objects.last()
    context={
        'rigs':rigs,
        'pool':pool,
        'ethusd':12345,#TODO ethusd.price
    }
    return render(request,'info/index.html',context)