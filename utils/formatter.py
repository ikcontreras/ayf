import pandas


class Formatter:
    @staticmethod
    def to_date_time(value: pandas.Timestamp):
        return value.tz_convert('CET').strftime("%Y-%m-%d %I:%M %p CET")