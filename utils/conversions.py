class Conversions:
    @staticmethod
    def to_dollars(value: float):
        return "${:,.2f}".format(value)

    @staticmethod
    def identify_billion(value: float):
        if value >= 1_000_000_000_000_000:
            value = value / 1_000_000_000_000_000
            return Conversions.to_dollars(value) + " Qa"
        if value >= 1_000_000_000_000:
            value = value / 1_000_000_000_000
            return Conversions.to_dollars(value) + " T"
        if value >= 1_000_000_000:
            value = value / 1_000_000_000
            return Conversions.to_dollars(value) + " B"
        elif value >= 1_000_000:
            value = value / 1_000_000
            return Conversions.to_dollars(value) + " M"
        else:
            return Conversions.to_dollars(value)