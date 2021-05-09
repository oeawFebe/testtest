timeout /t 30
cd C:\Users\Owner\Downloads\NBMiner_Win && nbminer --temperature-limit 75 --api 127.0.0.1:8001 --long-format --log-file nblog.log -a ethash -o ethproxy+tcp://eth-us.sparkpool.com:3333 -u 0x2a9ddcd3a4fa02b312512310087243c6f2591bc3.godlike
