# from src.multilevel_inheritance.two_wheeler import TwoWheeler


class Bike(object):
    """
    Single Inheritance Parent Class
    """

    def __init__(self, name, model, milage):
        self.name=name
        self.model=model
        self.milage=milage




    def get_milage(self):
        return self.milage

    def get_model(self):
        return self.model
    def get_name(self):
        return self.name

    def get_tank_capasity(self):
        return 0

