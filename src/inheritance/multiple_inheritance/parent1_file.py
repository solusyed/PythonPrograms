class Parent1File:

    def __init__(self, start, end, mid):
        self.start = start
        self.end = end
        self.mid = mid

    def get_start(self):
        return self.start

    def display_values(self):
        print(self.start, self.mid, self.end)
