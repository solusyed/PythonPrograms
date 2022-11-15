from src import swift


class Tesla(swift):
    def __init__(self,name,colour,model,milage,design):
        super(Tesla, self).__init__(name,colour,model,milage)
        self.design=design

        def get_design(self):
            return self.design