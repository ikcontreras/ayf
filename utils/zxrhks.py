import yfinance as yf

class Zxrhks:
    def __init__(self, ticker: str):
        self.ticker = yf.Ticker(ticker)

    def get_options(self, last_expiration_contract: str | None = None):
        if last_expiration_contract is None:
            return self.ticker.option_chain(self.ticker.options[0])
        return self.ticker.option_chain(last_expiration_contract)