import iso6346
# works start here

class ShippingContiner:
    ## adding the class attribute
    
    next_serial = 1337
    
    
    @classmethod
    def _generate_serial(cls):
        
       ## its almost same as the static method
       ## clss methoid
        
        result = cls.next_serial
        cls.next_serial +=1
        return result 
    
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code=owner_code,serial=str(serial).zfill(6)
        )
    
    ## you can make a class object using the class method
    ## when this method is called in the class
    ## it itself create  a object
    # when you cll the clas method with the
    ## parameter it will create a shipping container object
    ## it also works as a constructor
    ## and it can be used with initialize the class with 
    ## different different parameter
    @classmethod
    def create_empty(cls,owner_code):
        return cls(owner_code,contents=[])
    
    @classmethod
    def create_with_default(cls,contents):
        cls.owner_code = "bd"
        return cls(cls.owner_code,contents)
    
    @classmethod
    def create_with_items(cls,owner_code,items):
        return cls(owner_code,contents=list(items))
    
    
    
    ## this is the dunder init (connstructor method)
    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        ## class attribute shuld be called with the 
        ## after the clas method
        
        self.bic = ShippingContiner._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContiner._generate_serial()
            
        )
        
        
        
        
def main():
    ## inside the class the attribute value is tracked
    ## so in gets incrememted
    
    # c1 = ShippingContiner('YML',["books"])
    # print(c1.next_serial)
    # c2 = ShippingContiner('BD',["medicine"])
    # print(c2.next_serial)
    # c3 = ShippingContiner.create_empty("BD")
    # print(c3.owner_code)
    # print(c3.contents)
    # c3 = ShippingContiner.create_with_default(['books','water','cloth'])
    # print(c3.owner_code)
    # print(c3.contents)
    
    # c5 =ShippingContiner.create_with_items("MAE",["food",'Books','cloth'])
    # print(c5.contents)
    c = ShippingContiner.create_empty("YML")
    print(c.bic)
main()

    