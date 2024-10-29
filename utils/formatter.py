import pandas


class Formatter:
    @staticmethod
    def to_date_time(value: str):

        return pandas.to_datetime(value).tz_convert('CET').strftime("%Y-%m-%d %I:%M %p CET")