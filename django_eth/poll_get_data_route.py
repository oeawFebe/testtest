from fabric.api import local
import time
while True:
    local('curl http://localhost:8000/get_data')
    time.sleep(60)
