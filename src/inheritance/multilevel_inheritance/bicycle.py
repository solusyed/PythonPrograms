from src.inheritance.multilevel_inheritance.vehicle import Vehicle


class BiCycle(Vehicle):
    def __init__(self, name, gear):
        super(BiCycle, self).__init__(name, 'Two Wheeler')
        self.gear = gear