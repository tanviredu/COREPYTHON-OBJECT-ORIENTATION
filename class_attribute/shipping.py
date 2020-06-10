# works start here

class ShippingContiner:
    ## adding the class attribute
    
    next_serial = 1337
    
    
    @staticmethod
    def _generate_serial():
        
        ## first return then increment the value
        ## not return the increented value
        
        result = ShippingContiner.next_serial
        ShippingContiner.next_serial +=1
        return result 
    
    ## this is the dunder init (connstructor method)
    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        ## class attribute shuld be called with the 
        ## after the clas method
        
        self.serial = ShippingContiner._generate_serial()
        
        
        
        
def main():
    ## inside the class the attribute value is tracked
    ## so in gets incrememted
    
    c1 = ShippingContiner('YML',["books"])
    print(c1.next_serial)
    c2 = ShippingContiner('BD',["medicine"])
    print(c2.next_serial)
  
main()

    