import pandas as pd
import yfinance as yf

def fetch_data(tickers: list[str], period: str = "max", interval: str = "1d") -> pd.DataFrame:
    """Haal historische koersen op via yfinance, schrijf de Close-koersen naar data/prices.csv en geef ze terug."""
    historic_stock_prices = yf.download(tickers, period=period, interval=interval)

    close_prices = historic_stock_prices["Close"]

    close_prices_clean = close_prices.dropna(axis=0, how='any')

    close_prices_clean.to_csv("data/prices.csv")

    return close_prices_clean

def fetch_daily_data(tickers: list[str]) -> pd.DataFrame:
    """Versimpelde aanroep van fetch_data: maximale periode en een interval van 1 dag."""
    return fetch_data(tickers, period="max", interval="1d")

fetch_daily_data(["EMIM.AS", "IWDA.AS", "IUSN.DE"])
