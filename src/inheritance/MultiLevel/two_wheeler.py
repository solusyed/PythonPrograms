from src.MultiLevel.bicycle import BiCycle
from src.MultiLevel.hero_honda import HeroHonda
from src.MultiLevel.vehicle import Vehicle


class TwoWheeler(Vehicle):
    def __init__(self, name, engine_present):
        """

        :param name: string bike/ bycycle
        :param engine_present: boolean(True/False)
        """
        super(TwoWheeler, self).__init__(name, "Two Wheeler")
        self.engine_present = engine_present
        self.two_wheeler_object = None
        self.set_vehicle_object()

    def set_vehicle_object(self):
        if self.engine_present:
            self.two_wheeler_object = HeroHonda("Hero Honda", "Abc123", 123, 23)
        else:
            self.two_wheeler_object = BiCycle("hero", "2")


