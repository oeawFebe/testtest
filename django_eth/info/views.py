from django.shortcuts import render,redirect
from .models import Rig,Pool,ETHUSD
from selenium import webdriver
import time
import websocket
import ssl
import json
import cbpro
import datetime
import pytz
#
# def util_epoch_to_datetime(epochtime):
#     return  datetime.datetime.fromtimestamp(epochtime)

def index(request):

    rigs=[Rig.objects.latest('entry_datetime')]
    # TODO some sorting for unique rigs

    pool=Pool.objects.last()

    # geth the eth USD PRICE
    public_client=cbpro.PublicClient()
    price_dict=public_client.get_product_order_book("ETH-USD")
    print(price_dict)
    try:
        ethusd=(float(price_dict.get('bids')[0][0])+float(price_dict.get('asks')[0][0]))/2
    except:
        ethusd=0


    context={
        'rigs':rigs,
        'pool':pool,
        'ethusd':ethusd,
        'price_time':datetime.datetime.now(pytz.UTC)
    }
    return render(request,'info/index.html',context)

def get_data(request):
    URI = r"http://127.0.0.1:8001/api/v1/status"
    driver=webdriver.PhantomJS(r'C://webdriver/phantomjs.exe')
    driver.get(URI)
    time.sleep(1)
    partial_html = driver.execute_script("return document.getElementsByTagName('pre')[0].innerHTML")
    data_in_dict = json.loads(partial_html)
    device_dicts=data_in_dict.get('miner').get('devices')

    rig_data=Rig(
        name=data_in_dict.get('stratum').get('user').split('.')[1],

        is_power_on = bool(device_dicts[0].get('power','')),

        gpu_temp = max([x.get('temperature',0) for x in device_dicts]),
        realtime_hashrate = sum([float(x.get('hashrate','').split(' ')[0]) for x in device_dicts]),
        accepted_hashrate = sum([float(x.get('accepted_shares','')) for x in device_dicts]),
        lifetime_earning = 0, #
        costs = 6000,
    )
    rig_data.save()

    # get gas data secondly
    URL_gas='wss://www.gasnow.org/ws/gasprice'
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.connect(url=URL_gas)
    data=ws.recv()
    data_in_dict_gas = json.loads(data).get('data')
    pool_data = Pool(
        gasprice_rapid=int(data_in_dict_gas.get('rapid'))/10**9,
        gasprice_fast=int(data_in_dict_gas.get('fast')) / 10 ** 9,
        gasprice_standard=int(data_in_dict_gas.get('standard')) / 10 ** 9,
        gasprice_slow=int(data_in_dict_gas.get('slow')) / 10 ** 9,
    )
    pool_data.save()

    return redirect(index)