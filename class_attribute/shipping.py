# works start here

class ShippingContiner:
    ## adding the class attribute
    
    next_serial = 1337
    
    ## this is the dunder init (connstructor method)
    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        ## class attribute shuld be called with the 
        ## after the clas method
        
        self.serial = ShippingContiner.next_serial
        ## increment
        ## call the attribute with the Classname
        ShippingContiner.next_serial+=1 
        
        
        
        
def main():
    
    c1 = ShippingContiner('YML',["books"])
    print(c1.next_serial)
    c2 = ShippingContiner('BD',["medicine"])
    print(c2.next_serial)
  
main()

    