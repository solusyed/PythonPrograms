from src.car import Car


class Swift(Car):

    def __init__(self,name,milage,model,colour):
        super(Swift, self).__init__(name,milage,model)
        self.colour=colour

        def get_colour(self):
            return self.colour

        def get_design(self):
            return 0
