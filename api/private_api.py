import requests
import time
import hmac
import hashlib
import os
from urllib.parse import urlencode
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("BASE_URL")
PRIVATE_API_URL = os.getenv("PRIVATE_API_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def create_signature(params):
    """
    Создает подпись для запроса API.
    """
    body = urlencode(params).encode("utf-8")
    return hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()


def make_request(params):
    """
    Общая функция для выполнения запросов к API.
    """
    url = f"{BASE_URL}{PRIVATE_API_URL}"
    # Обновляем `nonce` для каждого запроса
    params["nonce"] = str(int(time.time()))
    sign = create_signature(params)

    headers = {"key": API_KEY, "sign": sign}

    response = requests.post(url=url, headers=headers, data=params)
    return response.json()


def get_private_info():
    """
    Метод возвращает информацию о балансах пользователя и привилегиях API-ключа, а так же время сервера (приватный API).
    """
    params = {
        "method": "getInfo",
    }

    return make_request(params)


def get_deposit_address(coin_name="btc"):
    """
    Метод возвращает адрес пополнения для указанной монеты (приватный API).
    """
    params = {
        "method": "GetDepositAddress",
        "coinName": coin_name,
        "need_new": 0,
    }

    return make_request(params)
