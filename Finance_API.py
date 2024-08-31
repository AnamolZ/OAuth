import asyncio
from fastapi import HTTPException
from Authenticator import get_current_user
from priceScrappy import StockInfoFetcher

class StockDataFetcher:
    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols

    def display_stock_info(self, stock_infos):
        for info in stock_infos:
            print(f"Symbol: {info['symbol']}, Price: {info['price']}")

    def fetch_stock_info(self):
        fetcher = StockInfoFetcher(self.stock_symbols)
        return fetcher.fetch_stock_info()

class TokenValidator:
    @staticmethod
    async def validate_access_token(token):
        try:
            return await get_current_user(token=token)
        except HTTPException as exc:
            return exc

async def main():
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        token = input("Enter your access token: ")
        validator = TokenValidator()
        user = await validator.validate_access_token(token)

        if isinstance(user, HTTPException):
            print("Access denied!")
            if attempt == max_attempts:
                print("Maximum attempts reached.")
                break
            else:
                print(f"Attempt {attempt}/{max_attempts}. Please try again.")
        else:
            print("Access granted!")
            fetcher = StockDataFetcher(stock_symbols=["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA", "GOOG", "NVDA", "NFLX"])
            stock_infos = fetcher.fetch_stock_info()
            fetcher.display_stock_info(stock_infos)
            return

if __name__ == "__main__":
    asyncio.run(main())
