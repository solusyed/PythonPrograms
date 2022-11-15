class Fibonaci:
    def fibonacci(self):
        f0=0
        f1=1
        for i in range(5):
            f2=f0+f1
            print(f2)
            f0=f1
            f1=f2



ct=Fibonaci()
ct.fibonacci()