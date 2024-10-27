from utils.zxrhks import Zxrhks


class PutOption(Zxrhks):
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_max_open_interest_otm(self):
        puts = self.get_options().puts
        return puts[~puts['inTheMoney']]['openInterest'].max()

    def get_total_open_interest_otm(self):
        calls = self.get_options().puts
        return calls[~calls['inTheMoney']]['openInterest'].sum()