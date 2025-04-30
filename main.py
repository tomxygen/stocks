from fastapi import FastAPI
import yfinance as yf
import time

app = FastAPI()

@app.get("/")
def root():
    return "welcome to the stock API made with FastAPI"

@app.get("/how-it-works")
def how_it_works():
    return "simply type the domain or IP followed by /stock/ and the ticker"

@app.get("/stock/{ticker}")
def return_stock_val(ticker):
    begin = time.time()
    tickk = yf.Ticker(ticker).info['regularMarketPrice']
    print(tickk)
    end = time.time()
    return {'ticker': ticker, 'value': tickk, 'time': end-begin}