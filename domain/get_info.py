from utils.zxrhks import Zxrhks


class GetInfo(Zxrhks):
    def __init__(self, ticker: str):
        super().__init__(ticker)

    def last_price(self):
        return self.ticker.fast_info.last_price

    def get_last_expiration_contract(self):
        return self.ticker.options[0]