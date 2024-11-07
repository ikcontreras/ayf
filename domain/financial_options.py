import pandas

from utils.zxrhks import Zxrhks


class FinancialOptions(Zxrhks):
    def __init__(self, ticker, call_option, put_option):
        self.call_option = call_option
        self.put_option = put_option
        super().__init__(ticker)

    def get_max_open_interest_otm(self):
        return max(self.call_option.get_max_open_interest_otm(), self.put_option.get_max_open_interest_otm())

    def get_strike_of_max_open_interest_otm(self):
        calls = self.get_options().calls
        puts = self.get_options().puts
        option = pandas.concat([calls, puts], ignore_index=True)
        return option.loc[option['openInterest'].idxmax(), 'strike']

    def get_last_price_otm(self):
        calls = self.get_options().calls
        puts = self.get_options().puts
        option = pandas.concat([calls, puts], ignore_index=True)
        return option.loc[option['openInterest'].idxmax(), 'lastPrice']

    def get_max_volume_otm(self):
        calls = self.get_options().calls
        puts = self.get_options().puts
        option = pandas.concat([calls, puts], ignore_index=True)
        return option.loc[option[~option['inTheMoney']]['openInterest'].idxmax(), 'volume']

    def get_sum_volume_otm(self):
        calls = self.get_options().calls
        puts = self.get_options().puts
        option = pandas.concat([calls, puts], ignore_index=True)
        return option[~option['inTheMoney']]['volume'].sum()

