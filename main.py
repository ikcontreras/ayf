import uvicorn
from fastapi import FastAPI, HTTPException

from domain.call_option import CallOption
from domain.financial_options import FinancialOptions
from domain.get_info import GetInfo
from domain.put_option import PutOption

app = FastAPI()

@app.get("/api/v1/ping")
def test_ping():
    return "pong"

@app.get("/api/v1/{ticker}/last_price")
def get_last_price(ticker: str):
    response = GetInfo(ticker).last_price()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return response

@app.get("/api/v1/{ticker}/last_expiration_contract")
def get_last_expiration_contract(ticker: str):
    response = GetInfo(ticker).get_last_expiration_contract()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return response

@app.get("/api/v1/{ticker}/call_option/total_open_interest/otm")
def get_total_open_interest_otm_calls(ticker: str):
    response = CallOption(ticker).get_total_open_interest_otm()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return float(response)

@app.get("/api/v1/{ticker}/put_option/total_open_interest/otm")
def get_total_open_interest_otm_calls(ticker: str):
    response = PutOption(ticker).get_total_open_interest_otm()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return float(response)

@app.get("/api/v1/{ticker}/call_option/max_open_interest/otm")
def get_total_open_interest_otm_calls(ticker: str):
    response = CallOption(ticker).get_max_open_interest_otm()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return float(response)

@app.get("/api/v1/{ticker}/put_option/max_open_interest/otm")
def get_total_open_interest_otm_calls(ticker: str):
    response = PutOption(ticker).get_max_open_interest_otm()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return float(response)

@app.get("/api/v1/{ticker}/option/max_open_interest/otm")
def get_strike_of_max_open_interest_otm(ticker: str):
    option = FinancialOptions(ticker, CallOption(ticker), PutOption(ticker))
    if option is None:
        raise HTTPException(status_code=404, detail="Not Found option")
    return float(option.get_max_open_interest_otm())

@app.get("/api/v1/{ticker}/option/strike_of_max_open_interest/otm")
def get_strike_of_max_open_interest_otm(ticker: str):
    option = FinancialOptions(ticker, CallOption(ticker), PutOption(ticker))
    if option is None:
        raise HTTPException(status_code=404, detail="Not Found max put interest")
    return float(option.get_strike_of_max_open_interest_otm())

@app.get("/api/v1/{ticker}/option/last_price/otm")
def get_last_price_otm(ticker: str):
    option = FinancialOptions(ticker, CallOption(ticker), PutOption(ticker))
    if option is None:
        raise HTTPException(status_code=404, detail="Not Found max put interest")
    return float(option.get_last_price_otm())

@app.get("/api/v1/{ticker}/beta")
def get_beta(ticker: str):
    response = GetInfo(ticker).get_beta()
    if response is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return float(response)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)



