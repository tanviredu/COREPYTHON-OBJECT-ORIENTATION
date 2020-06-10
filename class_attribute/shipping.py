# works start here

class ShippingContiner:
    ## this is the dunder init (connstructor method)
    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        
        
        
        
def main():
    c1 = ShippingContiner('YML',"books")
    c2 = ShippingContiner("BD","crops")
    print(c1.owner_code)
    print(c2.contents)    
main()

    