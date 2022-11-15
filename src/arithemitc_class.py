class ArithmeticClass:
    """
    Simple class to operate atithemtic operations
    """
    first_num = 20
    second_num = 40

    def get_sum_of_two_num(self):
        """
        Addition of two numbers
        :return: int
        """
        return self.first_num + self.second_num

    def get_mul_of_two_num(self):
        """
        multiplication of two numbers
        :return: int
        """
        return self.first_num * self.second_num

    def get_sub_of_two_num(self):
        """
        substraction of two numbers
        :return: int
        """
        return self.second_num - self.first_num

    def get_div_of_two_num(self):
        """
        divison of two numbers
        :return: float
        """
        return self.first_num / self.second_num

    def print_mulitplication(self):
        for item in range(1, 11):
            print("{} * {} = {}".format(self.first_num, item, self.first_num*item))

ac = ArithmeticClass() # memory allocation(Object creation)
res = ac.get_sum_of_two_num()
print(res)
print(res+40)
print(res/5)

ac.print_mulitplication()