# from rooms import A, B, C
#
#
# from obsevers.fire import FireStation
#
# fire_station = FireStation()
#
# a = A(fire_station)
# fire_station.subscribe(a)
#
# b = B(fire_station)
# fire_station.subscribe(b)
#
# c = C(fire_station)
# fire_station.subscribe(c)
#
#
# a.fire()


class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


f = Fib(1000)
f.a = 0
f.b = 1

print(next(f))
print(next(f))
print(next(f))




