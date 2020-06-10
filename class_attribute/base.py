class Base:
    def __init__(self):
        print("base initializer") 
        
    def f(self):
        print("called from the base")
        
        
class Sub(Base):
    
    # add initializer in the base class
    
    def __init__(self):
        
        ## to call the base initializer
        super().__init__()
        print("init from the sub")
    
    ## ovverrite the function    
    def f(self):
        print("called from the sub")
        


    



s = Sub()
s.f()