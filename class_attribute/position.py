class Position:
    
    def __init__(self,latitude,longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError("Latitude {} is out of range".format(latitude))
        
        if not (-180 <= longitude <= +180):
            raise ValueError("Longitude {} is out of range".format(longitude))
        
        self._latitude = latitude
        self._logitude = longitude
        
        
    
    @property 
    def latitude(self):
        return self._latitude
    
    
    @property
    def longitude(self):
        return self._logitude
        
    
    def __repr__(self):
        return f"Position(latitude = {self.latitude},longitude =  {self.longitude})"
    
    def __str__(self):
        return "position {}".format(self.latitude)
        
    def __format__(self, format_spec):
        return "hello"
        
        
oslo = Position(60.0,10.7)


news = Position(10.0,10.7)
q1 = repr(news)
q2 = str(news)
q3 = format(news)
print(q1)
print(q2)
print(q3)
print(news)