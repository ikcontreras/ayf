from utils.zxrhks import Zxrhks


class PutOption(Zxrhks):
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_max_open_interest_otm(self):
        puts = self.get_options().puts
        return puts[~puts['inTheMoney']]['openInterest'].max()

    def get_total_open_interest_otm(self):
        puts = self.get_options().puts
        return puts[~puts['inTheMoney']]['openInterest'].sum()

    def get_total_volume_otm(self):
        puts = self.get_options().puts
        return puts[~puts['inTheMoney']]['volume'].sum()