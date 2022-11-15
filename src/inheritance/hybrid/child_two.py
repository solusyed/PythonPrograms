from src.inheritance.hybrid.ancistor import Ancistor


class Child2(Ancistor):
    def __init__(self,name, age, compnies):
        super(Child2, self).__init__(name, age)
        self.companies=compnies

    def get_companies(self):
        return self.companies
