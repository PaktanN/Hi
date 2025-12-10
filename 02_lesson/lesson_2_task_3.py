import math

def square(side):
    area = side ** 2
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

print(square(4))  
print(square(3.2)) 