class BattlefieldHelper():

    def __init__(self):
        pass

    @staticmethod
    def is_in_bounds(x, y, battlefield):
        return battlefield.width() > x >= 0 and battlefield.height() > y >= 0