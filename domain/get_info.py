from utils.zxrhks import Zxrhks


class GetInfo(Zxrhks):
    def __init__(self, ticker: str):
        super().__init__(ticker)

    def last_price(self):
        return self.ticker.fast_info.last_price

    def get_last_expiration_contract(self):
        return self.ticker.options[0]

    def get_beta(self):
        return self.ticker.info['beta']

    def get_name_company(self):
        return self.ticker.info['longName']

    def get_sector(self):
        return self.ticker.info['sector']

    def get_market_cap(self):
        return self.ticker.fast_info.market_cap

    def get_earnings_call_time(self):
        return self.ticker.earnings_dates['EPS Estimate'].dropna().sort_index(ascending=False).first_valid_index()