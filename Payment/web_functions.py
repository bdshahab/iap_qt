from datetime import datetime, timezone
from decimal import Decimal
import requests

import sys
import os
import socket
import subprocess

from Payment.iap_variables import TESTING
# from Payment.payment import TESTING

# this one depends on selected coin
price_site_middle = ""

GITHUB = "https://raw.githubusercontent.com/bdshahab/iap_qt/main/"
DEFAULT_PRICE_KEYWORD = "default%20prices/"
DEFAULT_PRICE_SUFFIX = ".txt"
KEY_DATA_SITE_1 = GITHUB + "key_data_1.txt"
KEY_DATA_SITE_2 = GITHUB + "key_data_2.txt"
KEY_DATA_SITE_3 = GITHUB + "key_data_3.txt"
# updatable key data
IAP_VERSION = "9"

data = []
coin_icons = []
all_address = []
selected_coin_name = []
selected_coin_icon = []
selected_coin_address = []

def get_latest_key_data(url):
    response = get_with_fallback(url)
    the_result = response.text
    num = 1
    data.clear()
    for line in the_result.split("\n"):
        data.append(line)
        if num == 1:
            if line != IAP_VERSION:
                if line[0] == "-": # The app is under repair.
                    return -1
                elif line == "free": # The app is currently free.
                    return -2
                return False
        num = num + 1
    #update_urls()
    return True

def detect_system_proxy():
    proxies = {}

    for var in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"]:
        if var in os.environ:
            proxies["http"] = os.environ[var]
            proxies["https"] = os.environ[var]
            return proxies

    if sys.platform == 'darwin':
        try:
            output = subprocess.check_output(["scutil", "--proxy"], text=True)
            if "HTTPEnable : 1" in output:
                host = output.split("HTTPProxy : ")[1].split("\n")[0].strip()
                port = output.split("HTTPPort : ")[1].split("\n")[0].strip()
                if host and port:
                    return {
                        "http": f"http://{host}:{port}",
                        "https": f"http://{host}:{port}"
                    }
        except Exception:
            pass

    if os.name == 'nt':
        try:
            import winreg
            reg = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
            )
            enabled, _ = winreg.QueryValueEx(reg, "ProxyEnable")
            if enabled:
                server, _ = winreg.QueryValueEx(reg, "ProxyServer")
                if server:
                    return {
                        "http": f"http://{server}",
                        "https": f"http://{server}"
                    }
        except Exception:
            pass

    try:
        mode = subprocess.check_output(
            ["gsettings", "get", "org.gnome.system.proxy", "mode"],
            text=True
        ).strip("' \n")

        if mode == "manual":
            host = subprocess.check_output(
                ["gsettings", "get", "org.gnome.system.proxy.http", "host"],
                text=True
            ).strip("' \n")
            port = subprocess.check_output(
                ["gsettings", "get", "org.gnome.system.proxy.http", "port"],
                text=True
            ).strip()

            if host and port != "0":
                return {
                    "http": f"http://{host}:{port}",
                    "https": f"http://{host}:{port}",
                }
    except Exception:
        pass

    try:
        mode = subprocess.check_output(
            ["kreadconfig5", "--file", "kioslaverc", "--group", "Proxy Settings", "--key", "ProxyType"],
            text=True
        ).strip()

        if mode == "1":
            http_proxy = subprocess.check_output(
                ["kreadconfig5", "--file", "kioslaverc", "--group", "Proxy Settings", "--key", "httpProxy"],
                text=True
            ).strip()

            if http_proxy:
                parts = http_proxy.split()
                if len(parts) == 2:
                    host = parts[0].split("://")[1]
                    port = parts[1]
                    return {
                        "http": f"http://{host}:{port}",
                        "https": f"http://{host}:{port}"
                    }
    except Exception:
        pass

    try:
        active_conns = subprocess.check_output(
            ["nmcli", "-t", "-f", "NAME", "con", "show", "--active"],
            text=True
        ).strip()

        if active_conns:
            active = active_conns.split('\n')[0]
            full_output = subprocess.check_output(
                ["nmcli", "con", "show", active],
                text=True
            )

            proxy_method = None
            http_proxy = None
            for line in full_output.splitlines():
                if line.startswith('proxy.method:'):
                    proxy_method = line.split(':', 1)[1].strip()
                elif line.startswith('proxy.http-proxy:'):
                    http_proxy = line.split(':', 1)[1].strip()

            if proxy_method == 'manual' and http_proxy:
                return {
                    "http": f"http://{http_proxy}",
                    "https": f"http://{http_proxy}"
                }
    except Exception:
        pass

    return None

def is_port_open(port, timeout=0.2):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect(("127.0.0.1", port))
        s.close()
        return True
    except Exception:
        return False

def detect_tor():
    if is_port_open(9150):
        return {"http": "socks5h://127.0.0.1:9150", "https": "socks5h://127.0.0.1:9150"}
    if is_port_open(9050):
        return {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
    return None

def get_with_fallback(url, timeout=(5, 10)):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
    }
    proxy_chain = [
        None,
        detect_tor(),
        detect_system_proxy(),
    ]

    last_exc = None
    for proxy in proxy_chain:
        try:
            response = requests.get(url, proxies=proxy, timeout=timeout, headers=headers)
            response.raise_for_status()
            return response
        except Exception as e:
            last_exc = e

    raise last_exc or ValueError("All connection attempts failed")

def get_just_number(text_num: str):
    text_num = text_num.replace(",", "")
    return text_num

def get_coin_default_price(the_coin):
    the_url = GITHUB + DEFAULT_PRICE_KEYWORD + the_coin + DEFAULT_PRICE_SUFFIX
    response = get_with_fallback(the_url)
    return response.text  # Return the content as a string

def get_time_in_seconds(the_text_time):
    parts = the_text_time.split(":")
    hours = int(parts[0]) * 60 * 60
    minutes = int(parts[1]) * 60
    seconds = int(parts[2])
    return hours + minutes + seconds

def is_time_in_duration(the_text_time, first_time, last_time):
    the_time = get_time_in_seconds(the_text_time)
    the_first_time = get_time_in_seconds(first_time)
    the_last_time = get_time_in_seconds(last_time)
    return the_first_time <= the_time <= the_last_time

def format_with_separator(number, decimal_places=8, separator=','):
    number = float(str(number))
    formatted = f"{number:,.{decimal_places}f}"
    formatted = formatted.replace(',', separator)
    return formatted

def format_with_separator_without_extra_zeros_in_right(number, decimal_places=8, separator=','):
    number = float(str(number))
    formatted = f"{number:,.{decimal_places}f}"
    formatted = formatted.replace(',', separator)
    try:
        while formatted[-1] == "0" or formatted[-1] == ".":
            formatted = formatted[:-1]
    except Exception:
        formatted = "0"
    return formatted

def get_data_eth(the_api_url, the_api_key, the_txid):
    params = {
        data[6]: int(data[7]),  # Ethereum Mainnet
        data[8]: data[9],
        data[10]: data[11],
        data[12]: the_txid,
        data[13]: the_api_key
    }

    resp = requests.get(the_api_url, params=params).json()

    # ALWAYS validate
    if not isinstance(resp.get(data[14]), dict):
        raise RuntimeError(f"Etherscan error: {resp}")

    tx = resp[data[14]]

    to_address = tx[data[15]]
    wei = int(tx[data[16]], 16)
    input_amount = wei / Decimal("1000000000000000000")
    input_amount = format(input_amount, ".18f")

    block_hex = tx[data[17]]

    params_block = {
        data[18]: int(data[19]),
        data[20]: data[21],
        data[22]: data[23],
        data[24]: block_hex,
        data[25]: data[26],
        data[27]: the_api_key
    }

    block = requests.get(the_api_url, params=params_block).json()[data[14]]
    timestamp = int(block[data[28]], 16)

    timestamp = int(block[data[28]], 16)
    dt = datetime.fromtimestamp(timestamp, timezone.utc)
    the_result = {
        "DATE": dt.date(),
        "TIME": dt.time(),
        "INPUT_AMOUNT": input_amount,
        "RECEIVERS": to_address,
        }
    return the_result

# first_part_api_url: https://api.blockcypher.com/v1/
# second_part_api_url: /main/txs/
def get_data_btc_doge_ltc(first_part_api_url, second_part_api_url, the_coin, the_txid):
    url = first_part_api_url + the_coin + second_part_api_url + the_txid
    tx = requests.get(url, timeout=10).json()

    # Date & Time
    received_time = datetime.fromisoformat(
        tx.get(data[34], data[35]).replace(data[36], data[37])
    ).astimezone(timezone.utc)

    # Input value handler (cross-coin) 31
    def get_input_value(inp):
        return inp.get(data[38], inp.get(data[39], int(data[40])))

    total_input_sats = sum(get_input_value(i) for i in tx.get(data[41], []))
    total_input_coin = total_input_sats / 1e8  # convert satoshi-like units

    # Collect receivers safely
    receivers = set()
    for o in tx.get(data[42], []):
        addresses = o.get(data[43])
        if not addresses:  # handles None or empty
            continue
        for addr in addresses:
            receivers.add(addr)
    
    receivers = list(receivers)[0]
    the_time = str(received_time.time())
    if "." in the_time:
        the_time = the_time.split(".")[0]
    the_result = {
        "DATE":received_time.date(),
        "TIME":the_time,
        "INPUT_AMOUNT":total_input_coin,
        "RECEIVERS":receivers,
        }
    
    return the_result

def verify_payment(the_coin, the_address, the_price, the_txid, the_first_date, the_last_date, the_first_time, the_last_time):
    #!!!!!!!!!! TODO FBI
    try:
        if the_coin == "Ethereum (ETH)":
            the_address = the_address.lower()
            res = get_data_eth(data[4], data[5], the_txid)
            the_date = str(res.get("DATE"))
            the_time = str(res.get("TIME"))
            #? FOR TESTING
            if TESTING:
                the_address = "0xfBF1f357A4cEeE90D4c7Bc5f32A222fD6065f15a".lower()
                the_price = "0.084902310000000000"
                the_first_date = "2021-10-07"
                the_last_date = "2021-10-08"
                the_first_time = "20:00:29"
                the_last_time = "20:18:29"
                #????????????? END OF TESTING ?????????????
                print("-" * 20)
                print(f"the_coin: {the_coin}")
                print(f"the_address: {the_address}")
                print(f"the_price: {the_price}")
                print(f"the_txid: {the_txid}")
                print(f"the_first_date: {the_first_date}")
                print(f"the_last_date: {the_last_date}")
                print(f"the_first_time: {the_first_time}")
                print(f"the_last_time: {the_last_time}")
                print("+" * 20)
                print(f'res.get("RECEIVERS"): {res.get("RECEIVERS")}')
                print(f'res.get("DATE"): {res.get("DATE")}')
                print(f'res.get("TIME"): {res.get("TIME")}')
                print(f'res.get("INPUT_AMOUNT"): {res.get("INPUT_AMOUNT")}')
                print("*" * 20)
            if res.get("RECEIVERS") != the_address:
                return "ADDRESS"
            elif (the_date != the_first_date) and (the_date != the_last_date):
                return "DATE"
            elif not is_time_in_duration(the_time, the_first_time, the_last_time):
                return "TIME"
            elif str(res.get("INPUT_AMOUNT")) != the_price:
                return "PRICE"
        else:
            # Other crypto goes here
            # 
            if the_coin == "Bitcoin (BTC)":
                the_coin = data[31]
            elif the_coin == "Dogecoin (DOGE)":
                the_coin = data[32]
            elif the_coin == "Litecoin (LTC)":
                the_coin = data[33]
            res = get_data_btc_doge_ltc(data[29], data[30], the_coin, the_txid)
            the_date = str(res.get("DATE"))
            the_time = str(res.get("TIME"))
            if TESTING:
                print(f"the_coin: {the_coin}")
                if the_coin == "btc":
                    the_address = "1LQSzFZKE5vwiUS94toMG7r5M2nQ4X2muw"
                    the_price = "0.00381949"
                    the_first_date = "2019-10-02"
                    the_last_date = "2019-10-03"
                    the_first_time = "21:38:47"
                    the_last_time = "21:58:47"
                elif the_coin == "doge":
                    the_address = "DK7LpDSQQKgVa8wSepytUisKFW9fmQ1vmR"
                    the_price = "519.429489"
                    the_first_date = "2021-05-06"
                    the_last_date = "2021-05-07"
                    the_first_time = "13:46:42"
                    the_last_time = "14:06:42"
                elif the_coin == "ltc":
                    the_address = "LRQ6TBVXsEVPApbCY79bV1d9LR8E7JiuDd"
                    the_price = "0.00994753"
                    the_first_date = "2022-02-08"
                    the_last_date = "2022-02-09"
                    the_first_time = "06:54:57"
                    the_last_time = "07:14:57"
                #????????????? END OF TESTING ?????????????
                print("-" * 20)
                print(f"the_coin: {the_coin}")
                print(f"the_address: {the_address}")
                print(f"the_price: {the_price}")
                print(f"the_txid: {the_txid}")
                print(f"the_first_date: {the_first_date}")
                print(f"the_last_date: {the_last_date}")
                print(f"the_first_time: {the_first_time}")
                print(f"the_last_time: {the_last_time}")
                print("+" * 20)
                print(f'res.get("RECEIVERS"): {res.get("RECEIVERS")}')
                print(f'res.get("DATE"): {res.get("DATE")}')
                print(f'res.get("TIME"): {res.get("TIME")}')
                print(f'res.get("INPUT_AMOUNT"): {res.get("INPUT_AMOUNT")}')
                print("*" * 20)
            if res.get("RECEIVERS") != the_address:
                return "ADDRESS"
            elif (the_date != the_first_date) and (the_date != the_last_date):
                return "DATE"
            elif not is_time_in_duration(the_time, the_first_time, the_last_time):
                return "TIME"
            elif str(res.get("INPUT_AMOUNT")) != the_price:
                return "PRICE"
    except Exception:
        return "TXID"
    return "OK"
