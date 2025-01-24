import requests
import json


BASE_URL = "https://yobit.net/api/3"


def save_to_file(filename, data):
    """
    Сохраняет данные в JSON файл
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def fetch_data(url):
    """
    Выполняет запрос к указанному URL и возвращает ответ
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Выбросит исключение при ошибке HTTP
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def get_info():
    """
    Получает информацию обо всех актуальных парах криптовалют на бирже
    """
    response = fetch_data(f"{BASE_URL}/info")
    data = response.json()
    save_to_file("output/info.json", data)
    return data


def get_ticker(base_currency="btc", quote_currency="usdt"):
    """
    Получает информацию о паре (парах) криптовалют за последние 24 часа
    """
    # response = requests.get(f"{BASE_URL}/ticker/btc_usdt-eth_usdt-xrp_usdt?ignore_invalid=1")
    response = fetch_data(
        f"{BASE_URL}/ticker/{base_currency}_{quote_currency}?ignore_invalid=1"
    )
    data = response.json()
    save_to_file("output/ticker.json", data)
    return data


def get_depth(base_currency="btc", quote_currency="usdt", limit=150):
    """
    Получает информацию выставленных на продажу и покупку ордерах
    limit - количество ордеров

    Респонс:
    asks - словарь с оредрами на продажу
    bids - словарь с оредрами на покупку
    0: прайс
    1: количество монет, готовых уйти на продажу или покупку
    """
    response = fetch_data(
        f"{BASE_URL}/depth/{base_currency}_{quote_currency}?limit={limit}&ignore_invalid=1"
    )
    data = response.json()
    save_to_file("output/depth.json", data)

    bids = data[f"{base_currency}_{quote_currency}"]["bids"]

    total_bid_volume = 0
    for bid in bids:
        price = bid[0]
        coin_amount = bid[1]

        total_bid_volume += price * coin_amount

    return f"Total bids amount {base_currency}_{quote_currency}: {total_bid_volume} $"


def get_trades(base_currency="btc", quote_currency="usdt", limit=150):
    """
    Получает информацию о совершенных сделках о покупке и продаже
    asks: selling orders
    bids: buying orders
    """
    response = fetch_data(
        f"{BASE_URL}/trades/{base_currency}_{quote_currency}?limit={limit}&ignore_invalid=1"
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


def main():
    # print(get_info())
    # print(get_ticker(base_currency="xrp"))
    # print(get_depth(base_currency="xrp", limit=2000))
    # print(get_trades(base_currency="xrp", limit=2000))
    # print(get_trades(base_currency="xrp", limit=2000))

    base_currency = input("Enter a coin name: ")
    print(get_trades(base_currency=base_currency))


if __name__ == "__main__":
    main()
