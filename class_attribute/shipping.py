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
    def create_empty(cls,owner_code,**kwargs):
        return cls(owner_code,contents=[],*kwargs)
    
    
    
    
    
    @classmethod
    def create_with_default(cls,contents):
        cls.owner_code = "bd"
        return cls(cls.owner_code,contents)
    
    @classmethod
    def create_with_items(cls,owner_code,items,**kwargs):
        return cls(owner_code,contents=list(items),**kwargs)
    
    
    
    ## this is the dunder init (connstructor method)
    def __init__(self,owner_code,contents,**kwargs):
        self.owner_code = owner_code
        self.contents = contents
        ## class attribute shuld be called with the 
        ## after the clas method
        
        
        ## now it will read the property of the refrigaretor class
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContiner._generate_serial()
            
        )
        



class ReGrigetorShippingContainer(ShippingContiner):
    
    
    MAX_CELCIUS = 4.0
    
    def __init__(self,owner_code,contents,*,celsius,**kwargs):
        super().__init__(owner_code,contents,**kwargs)
        self.celsius = celsius
        
        
        
    
    ## getter and setter for the farenheit
    
    @property
    def farenheit(self):
        return ReGrigetorShippingContainer._c_to_f(self.celsius)
    
    @farenheit.setter
    def farenheit(self,value):
        self.celsius = ReGrigetorShippingContainer._f_to_c(value)
    
    
        
    # adding converting static method
    
    @staticmethod
    def _c_to_f(celsius):
        return celsius *9/5 +32
    
    @staticmethod
    
    def _f_to_c(farenheit):
        return (farenheit -32) *5/9    
        
        
        
    
    
        
    
    
    ## this is the getter    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self,value):
        if(value > ReGrigetorShippingContainer.MAX_CELCIUS):
            raise ValueError("Temparutere is hot")
        
        self._celsius = value
    
    ## overwriting the static method
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial=str(serial).zfill(6),
            category="R"
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
    # c = ShippingContiner.create_empty("YML")
    # print(c.bic)
    # print(ShippingContiner._make_bic_code("MAE",'1234'))
    
    
    ## this use the parent init dunder method
    #r1 = ReGrigetorShippingContainer("MAE",['fish'])
    #print(r1.bic)
    ## this use new class method
    # print(ReGrigetorShippingContainer._make_bic_code('MAE',1234))
    
    # c = ShippingContiner("MAE",['textile'])
    # print(c._make_bic_code("MAE",1234))
    # r = ReGrigetorShippingContainer("MAE",['peas'])
    # print(r._make_bic_code("MAE",1234))
    r3 = ReGrigetorShippingContainer.create_with_items('ESC',['onions'],celsius=2.0)
    print(r3.contents)
    print(r3.celsius)
    r3.celsius = 2
    print(r3.celsius)
main()

    