<<<<<<< HEAD
class filterprime:
    def init(self, a):
        self.a = a

    def filter_prime(y):
        y=[]
        for i in range(len(a)):
           if a[i] == 1:
                continue
           t = True
           for j in range(2, a[i]):
                if a[i] % j == 0:
                   t = False
                   break
           if t == True:
                y.append(a[i])
        print(y)

a = [int(x) for x in input().split()]
print(a)
p = filterprime(a)
=======
class filterprime:
    def init(self, a):
        self.a = a

    def filter_prime(y):
        y=[]
        for i in range(len(a)):
           if a[i] == 1:
                continue
           t = True
           for j in range(2, a[i]):
                if a[i] % j == 0:
                   t = False
                   break
           if t == True:
                y.append(a[i])
        print(y)

a = [int(x) for x in input().split()]
print(a)
p = filterprime(a)
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
p.filter_prime()