from src.inheritance.multilevel_inheritance.bike import Bike


class HeroHonda(Bike):
    """
    Child Class HeroHonda, and aquired parent Bike properties to Child class

    """

    def __init__(self, name, model, milage, tank_capasity):
        super(HeroHonda, self).__init__(name, model, milage)
        self.tank_capasity = tank_capasity

    def get_tank_capasity(self):
        return self.tank_capasity