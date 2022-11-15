from src.inheritance.hybrid.child1 import Child1


class Subchild2(Child1):
    def __init__(self, name, age, dresses, watches):
        super(Subchild2, self).__init__(name, age, dresses)
        self.watches=watches


    def get_watches(self):
        return self.watches