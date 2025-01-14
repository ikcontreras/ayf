from utils.zxrhks import Zxrhks


class CallOption(Zxrhks):
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_max_open_interest_otm(self):
        calls = self.get_options().calls
        return calls[~calls['inTheMoney']]['openInterest'].max()

    def get_total_open_interest_otm(self):
        calls = self.get_options().calls
        return calls[~calls['inTheMoney']]['openInterest'].sum()

    def get_total_volume_otm(self):
        calls = self.get_options().calls
        return calls[~calls['inTheMoney']]['volume'].sum()