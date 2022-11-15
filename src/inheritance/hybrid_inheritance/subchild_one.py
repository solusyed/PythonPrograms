from src.inheritance.hybrid_inheritance.child_one import Child1


class Subchild1(Child1):
    def __init__(self, name, age, dresses, brands):
        super(Subchild1, self).__init__(name, age, dresses)
        self.brands=brands

    def get_brands(self):
        return self.brands
