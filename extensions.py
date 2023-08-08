import json
import requests
from config import currencies

class ConvertionException(Exception):
    pass

class ConverterClass:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Нельзя конвертировать одинаковые валюты: {base}')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неверно введено количество: {amount}')

        responce = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        return float(json.loads(responce.content)[base_ticker]) * amount