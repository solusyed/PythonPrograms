"""
POlymorphism:
            polymorphism is nothing but a function can perform multiple functions.
               two types of polymorphism:
           1) static polymorphism(compile time)
           2) dynamic polymorphism(run time)

    static polymorphism:
             a single function can perform multipletask in a single class.
    dynamic polymorphism:
            a single function can perform multipletask in a multiple class.
        """
# dynamic polymorphism example:
class A:
    def display_method(self):
        a = 4
        print(a)



class B:
    def display_method(self):
        b = 6
        print(b)


a=B()
a.display_method()
b=A()
b.display_method()