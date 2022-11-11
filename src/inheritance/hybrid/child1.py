from src.inheritance.hybrid.ancistor import Ancistor


class Child1(Ancistor):
    def __init__(self, name, age, dresses):
        super(Child1, self).__init__(name, age)
        self.dresses=dresses


    def get_dresses(self):
        return self.dresses
