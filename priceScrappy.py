from bs4 import BeautifulSoup
import requests
import yfinance as yf
from datetime import datetime, timedelta
import os
import pandas as pd
import concurrent.futures

class StockPrice:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.url = f'https://finance.yahoo.com/quote/{stock_symbol}/'
        self.price = None

    def scrape_price(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
            self.price = float(price_tag.text) if price_tag else 'N/A'
        except requests.RequestException:
            self.price = None

    def history_training_data(self):
        try:
            today = datetime.utcnow()
            three_months_ago = today - timedelta(days=90)
            training_data = yf.download(self.stock_symbol, start=three_months_ago, end=today, interval='1d')
            training_data.to_csv('TrainingData.csv')
        except Exception:
            pass

    def process_data(self):
        try:
            if not os.path.isfile('TrainingData.csv'):
                self.history_training_data()
            stock_data = pd.read_csv('TrainingData.csv')
            stock_data['Date'] = pd.to_datetime(stock_data['Date'])
            stock_data.set_index('Date', inplace=True)
            stock_data['Volume'] = stock_data['Volume'].str.replace(",", "", regex=False).astype('Int64')
            stock_data = stock_data.apply(pd.to_numeric, errors='coerce').sort_index()
            stock_data.reset_index().to_csv('TrainingData.csv', index=False)
            one_month_ago = datetime.now() - timedelta(days=30)
            recent_data = stock_data.loc[one_month_ago:].reset_index()
            recent_data.to_csv('MonthlyData.csv', index=False)
        except Exception:
            pass

    def get_stock_info(self):
        self.scrape_price()
        return {'symbol': self.stock_symbol, 'price': self.price}

class StockInfoFetcher:
    def __init__(self, symbols):
        self.symbols = symbols

    def fetch_stock_info(self):
        stock_info_list = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(StockPrice(symbol).get_stock_info): symbol for symbol in self.symbols}
            for future in concurrent.futures.as_completed(futures):
                stock_info_list.append(future.result())
        return stock_info_list

if __name__ == "__main__":
    symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA", "GOOG", "NVDA", "NFLX"]
    fetcher = StockInfoFetcher(symbols)
    stock_infos = fetcher.fetch_stock_info()
    for info in stock_infos:
        print(f"Symbol: {info['symbol']}, Price: {info['price']}")
