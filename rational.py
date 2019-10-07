class Q(object) :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    # def fraction(self) :
    #     return(self.a / self.b)

    def __repr__(self) :
        return(str(self.a / self.b))

q = Q(1, 2)
print(q)