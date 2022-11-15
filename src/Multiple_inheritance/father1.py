"""Father              Father1
   cars, bikes          houses, lands


     Child
       cars, bikes, houses, lands """


class Father1(object):
    def __init__(self, cars, bikes):
        self.cars=cars
        self.bikes=bikes

    def get_cars(self):
        return self.cars

    def get_bikes(self):
        return self.bikes

