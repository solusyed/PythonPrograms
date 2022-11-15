from src.Multiple_inheritance.father1 import Father1
from src.Multiple_inheritance.father2 import Father2


class Child(Father1,Father2):
    def __init__(self, cars, bikes, houses, lands):
        Father1.__init__(self, cars, bikes)
        Father2.__init__(self, houses, lands)
