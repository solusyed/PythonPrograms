from src.inheritance.multilevel_inheritance.vehicle import Vehicle


class Bike(Vehicle):
    """
    Single Inheritance Parent Class
    """

    def __init__(self, name, model, milage):
        """
         Constructor with three parameter, Pass the values at the time of object creation
        :param name: bike name
        :param model: bike model
        :param milage: bike milage
        """
        super(Bike, self).__init__(name, "Two Wheeler")
        self.model = model
        self.milage = milage

    def get_milage(self):
        return self.milage

    def get_model(self):
        return self.model

    def get_tank_capasity(self):
        return 0

