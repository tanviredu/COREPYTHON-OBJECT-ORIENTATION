class SimpleList:
    
    def __init__(self,items):
        self._items = list(items)
        
    def add(self,item):
        self._items.append(item)
        
    def __getitem__(self,index):
        self._items[index]
        
    def sort(self):
        self._items.sort()
        
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f'{type(self).__name__} ({self._items!r})'
        
        
class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()  ## this is the generic sort method
        
    def add(self,item):
        super().add(item)
        return self.sort()
    


s = SortedList()
print(isinstance(s,SortedList))
print(isinstance(s,SimpleList))
print(isinstance(s,(SortedList,SimpleList)))



## make a list that only take the int

class IntList(SimpleList):
    def __init__(self,items=()):
        
        for x in items:
            self._validate(x)
            super().__init__(items)
            
    @staticmethod
    def _validate(x):
        if not isinstance(x,int):
            raise TypeError("it is not int")
        
    
    def add(self,item):
        self._validate(item)
        super().add(item)
        
    
print(issubclass(IntList,SimpleList))



# you want to ad both functionality in one class

class IntsortedList(SortedList,IntList):
    pass


fs = IntsortedList([6,5,4,4,3,2,"-1"])   ## it will show an an error
                                         ## it will check that if it is int
                                         ## if it is then it sort

