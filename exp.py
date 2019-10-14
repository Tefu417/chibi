class Expr :
    def eval(self) :
        pass
    
def expr(x):
    if not isinstance(x, Expr) :
        x = Val(x)
    return x

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
        self.left = expr(left)
        self.right = expr(right)

    def eval(self) :
        return self.left.eval() + self.right.eval()

class Mul(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
    
    def eval(self) :
        return self.left.eval() * self.right.eval()

class Sub(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
    
    def eval(self) :
        return self.left.eval() - self.right.eval()
    
class Div(Expr) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
        
    def eval(self) :
        return self.left.eval() // self.right.eval()

e = Add(1, Val(2))
assert e.eval () == 3
print("OK")