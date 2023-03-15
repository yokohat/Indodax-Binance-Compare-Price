import requests
import time
import datetime

while True:
    header = ["+---------BUSD---------+","+---------USDT---------+", "+---------BNB----------+", "+---------ETH----------+", "+---------END----------+"]
    time_print = datetime.datetime.now()
    # BUSD
    busd = "https://api.binance.me/api/v3/ticker/price?symbol=BUSDBIDR"
    response = requests.get(busd)
    busd = response.json()
    busd_idx = "https://indodax.com/api/ticker/busdidr"
    response = requests.get(busd_idx)
    busd_idx = response.json()

    # USDT
    usdt = "https://api.binance.me/api/v3/ticker/price?symbol=USDTBIDR"
    response = requests.get(usdt)
    usdt = response.json()
    usdt_idx = "https://indodax.com/api/ticker/usdtidr"
    response = requests.get(usdt_idx)
    usdt_idx = response.json()

    # BNB
    bnb = "https://api.binance.me/api/v3/ticker/price?symbol=BNBBIDR"
    response = requests.get(bnb)
    bnb = response.json()
    bnb_idx = "https://indodax.com/api/ticker/bnbidr"
    response = requests.get(bnb_idx)
    bnb_idx = response.json()

    # ETH
    eth = "https://api.binance.me/api/v3/ticker/price?symbol=ETHBIDR"
    response = requests.get(eth)
    eth = response.json()
    eth_idx = "https://indodax.com/api/ticker/ethidr"
    response = requests.get(eth_idx)
    eth_idx = response.json()

    print(header[0])
    print("BINANCE -", busd["price"])
    print("INDODAX -", busd_idx["ticker"]["last"])
    print(header[1])
    print("BINANCE -", usdt["price"])
    print("INDODAX -", usdt_idx["ticker"]["last"])
    print(header[2])
    print("BINANCE -", bnb["price"])
    print("INDODAX -", bnb_idx["ticker"]["last"])
    print(header[3])
    print("BINANCE -", eth["price"])
    print("INDODAX -", eth_idx["ticker"]["last"])
    print(header[4])
    print()
    print("+------", time_print.strftime("%H:%M:%S"), "------+")
    print()

    time.sleep(5)