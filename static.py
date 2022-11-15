# static polymorphism
#  perform multiple task using single function in single class.
class SumOfElements:
    def __init__(self):
        pass
    #def sumofelements(self,firstelement, secondelement):
        #return firstelement+secondelement
    def sumofelements(self,firstelement, secondelement, thirdelement = 0):
        return firstelement+secondelement+thirdelement

som=SumOfElements()
#som.sumofelements(4,5)
print(som.sumofelements(4,5,78))
