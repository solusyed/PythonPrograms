class SimpleClass:
    """
    Its SimpleCalss which return name, age and  static name and age
    """
    name = "shoail"
    age = 22

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


sc = SimpleClass()
print(sc.get_age())