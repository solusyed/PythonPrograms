"""
POlymorphism:
            polymorphism is nothing but a function can perform multiple functions.
               two types of polymorphism:
           1) static polymorphism(compile time)
           2) dynamic polymorphism(run time)
           """

#  1)  static polymorphism:
           #  a single function can perform multipletask in a single class.

# example:


class Father1(object):
    def __init__(self, cars, bikes):
        self.cars=cars
        self.bikes=bikes

    def get_cars(self):
        return self.cars

    def get_bikes(self):
        return self.bikes


fa=Father1("swift", "honda")
print(fa.get_cars())

print(fa.get_bikes())


