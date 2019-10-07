class Q(object) :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def __repr__(self) :
        if(self.b == 1) :
            return str(self.a)
        else :
            return f'{self.a} / {self.b}'

    def add(self, q) :  #self = q1, q = q2
        a = self.a * q.b + q.a * self.b
        b = self.b * q.b
        return Q(a, b)

    def sub(self, q) :
        a = self.a * q.b - q.a * self.b
        b = self.b * q.b
        return Q(a, b)

    def mul(self, q) :
        a = self.a * q.a
        b = self.b * q.b
        return Q(a, b)

q1 = Q(2, 5)
q2 = Q(1, 3)
print(q1.add(q2))