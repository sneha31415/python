# faster approach
from itertools import combinations as nCr

class Odometer:
    # READINGS contain all the readings of all the sizes 
    # i.e we generate readings only for the first odometer, this is checked by .FIRST_TIME
    READINGS = {}
    FIRST_TIME = True

    def __init__(self, size: int):
        if Odometer.FIRST_TIME:
            Odometer.FIRST_TIME = False
            for _size in range(2, 9):
                Odometer.READINGS[_size] = [''.join(_) for _ in nCr("123456789", _size)] 
        self.size = size
        self.position = 0
        self.readings = Odometer.READINGS[size]
        self.count = len(self.readings)
    
    def __repr__(self) -> str:
        r = self.readings[self.position]
        return f'{r} at {self.position} of {self.count}'
    
    def __str__(self) -> str:
        return f'{self.readings[self.position]}'
    
    def forward(self, steps: int = 1):
        self.position = (self.position + steps) % self.count

    def forward(self, steps: int = 1):
        self.position = (self.position - steps) % self.count

k = Odometer(3)
print(k)
print(repr(k))
k.forward


# team = 116 , 64, 11
