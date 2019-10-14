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

    def eval(self) :
        return self.left.eval() + self.right.eval()

v = Add(Add(Val(1), Val(2)),Val(3))
print(v.eval())
