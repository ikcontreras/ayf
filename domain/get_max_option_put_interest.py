from utils.zxrhks import Zxrhks


class GetMaxOptionPutInterest(Zxrhks):
    def __init__(self, ticker, call_option, put_option):
        self.call_option = call_option
        self.put_option = put_option
        super().__init__(ticker)

    def otm(self):
        return max(self.call_option.get_max_open_interest_otm(), self.put_option.get_max_open_interest_otm())