import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = os.getenv("BASE_URL")
PUBLIC_API_URL = os.getenv("PUBLIC_API_URL")


def save_to_file(filename, data):
    """
    Сохраняет данные в JSON файл
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def fetch_public_data(endpoint):
    """
    Выполняет запрос к публичному API и возвращает ответ
    """
    url = f"{BASE_URL}{PUBLIC_API_URL}{endpoint}"
    # print(f"Fetching data from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Выбросит исключение при ошибке HTTP
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching public data: {e}")
        return None


def get_info():
    """
    Получает информацию обо всех актуальных парах криптовалют на бирже (публичный API)
    """
    response = fetch_public_data("/info")
    data = response.json()
    save_to_file("output/info.json", data)
    return data


def get_ticker(base_currency="btc", quote_currency="usdt"):
    """
    Получает информацию о паре (парах) криптовалют за последние 24 часа (публичный API)
    """
    # response = requests.get(f"{BASE_URL}/ticker/btc_usdt-eth_usdt-xrp_usdt?ignore_invalid=1")
    response = fetch_public_data(
        f"/ticker/{base_currency}_{quote_currency}?ignore_invalid=1"
    )
    data = response.json()
    save_to_file("output/ticker.json", data)
    return data


def get_depth(base_currency="btc", quote_currency="usdt", limit=150):
    """
    Получает информацию выставленных на продажу и покупку ордерах (публичный API)
    """
    response = fetch_public_data(
        f"/depth/{base_currency}_{quote_currency}?limit={limit}&ignore_invalid=1"
    )
    data = response.json()
    save_to_file("output/depth.json", data)

    # ордера на покупку
    bids = data[f"{base_currency}_{quote_currency}"]["bids"]
    total_bid_volume = 0
    for bid in bids:
        price = bid[0]
        coin_amount = bid[1]
        # Общий объем покупок
        total_bid_volume += price * coin_amount

    return f"Total bids amount {base_currency}_{quote_currency}: {round(total_bid_volume, 2)} $"


def get_trades(base_currency="btc", quote_currency="usdt", limit=150):
    """
    Получает информацию о совершенных сделках о покупке (bid) и продаже (ask) (публичный API)
    """
    response = fetch_public_data(
        f"/trades/{base_currency}_{quote_currency}?limit={limit}&ignore_invalid=1"
    )
    data = response.json()
    save_to_file("output/trades.json", data)

    total_trade_ask = 0
    total_trade_bid = 0

    for trade in data[f"{base_currency}_{quote_currency}"]:
        if trade["type"] == "ask":
            total_trade_ask += trade["price"] * trade["amount"]
        elif trade["type"] == "bid":
            total_trade_bid += trade["price"] * trade["amount"]

    summary = f"[-] TOTAL {base_currency} SELL: {round(total_trade_ask, 2)} $ \n[+] TOTAL {base_currency} BUY: {round(total_trade_bid, 2)} $"
    return summary
