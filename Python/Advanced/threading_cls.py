from threading import Thread
import time
'''
print("begin")
class X(Thread):
    def run(self):
        for p in range(1,101):
            print(p)
            if p==50:
                print("i am waiting 10 sec")
                time.sleep(10)
                print("10 sec compleated")

class Y(Thread):
    def run(self):
        for q in range(101,201):
            print(q)

x1=X()
y1=Y()

x1.start()
y1.start()

for r in range(201,301):
    print(r)

'''

class X(Thread):
    def run(self):
        time.sleep(10)
        self.sum = 0
        for p in range(1,101):
            # print(p)
            self.sum = self.sum+p

class Y(Thread):
    def __init__(self, x1):
        super().__init__()
        self.x1=x1

    def run(self):
        for q in range(101,201):
            print(q)
            if q==120:
                self.x1.join()
                print(self.x1.sum)

x1=X()
y1=Y(x1)
x1.start()
y1.start()
