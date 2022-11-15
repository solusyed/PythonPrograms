class ParentFile:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def display_name(self):
        print(self.name)