import time
#OOP

class Tutorial:

    def __init__(self):
        self.mijngetal = 1
    
    def verhoog(self, getal):
        self.mijngetal += getal

tut = Tutorial()
tut.verhoog(5)
print(tut.mijngetal)

starttime = time.time()
temp = 0
for _ in range(10000):
    temp += 1
print(str(time.time() - starttime))