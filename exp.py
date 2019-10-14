class Expr :
    def eval(self) :
        pass

class Val(Expr) :
    __slots__ = ["value"]
    def __init__(self, value = 0) :
        self.value = value

    def eval(self) :
        return self.value

    def __repr__(self) :
        return f'Val({self.value})'

class Add(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right

    def eval(self) :
        return self.left.eval() + self.right.eval()

class Mul(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right
    
    def eval(self) :
        return self.left.eval() * self.right.eval()

class Sub(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right
    
    def eval(self) :
        return self.left.eval() - self.right.eval()
    
class Div(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = left
        self.right = right
        
    def eval(self) :
        return self.left.eval() // self.right.eval()

assert isinstance(Val(1), Expr)
assert isinstance(Div(Val(7), Val(2)), Expr)
print("OK")