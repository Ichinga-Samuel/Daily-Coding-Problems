"""Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. 
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), 
return the second instance."""


def singleton(cls):
    instance = [None, None]
    counter = 0
    @wraps(cls)
    def _singleton(*args, **kwargs):
        nonlocal counter, instance

        if counter > 1:
            counter = 0
            
        if instance[counter] is None:
            instance[counter] = cls(*args, **kwargs)           
        
        counter += 1
        return instance[counter-1]
    return _singleton


@singleton
class TwistedSingleton:
    
    def __init__(self, m):
        self.m = m
        self.w = m*2


a = TwistedSingleton(100)  
print(a.m)
b = TwistedSingleton(400)
print(b.m)
c = TwistedSingleton(200)
print(c.m)
d = TwistedSingleton(300)
print(d.m)

