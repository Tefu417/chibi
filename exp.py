class Val(object) :
    __slots__ = ["value"]
    def __init__(self, value = 0) :
        self.value = value

    def eval(self) :
        return self.value

    def __repr__(self) :
        return f'Val({self.value})'

class Add(object) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right

    # def expr(self) :
    #     if not hasattr(self, "eval") :
    #         self = Val(self)
    #     return self

    def eval(self) :
        return self.left.eval() + self.right.eval()

class Mul(object) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right
    
    def eval(self) :
        return self.left.eval() * self.right.eval()

class Sub(object) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right
    
    def eval(self) :
        return self.left.eval() - self.right.eval()


v = Sub(Val(1), Val(2))
assert v.eval() == -1
print("OK")