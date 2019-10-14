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
        return self.left + self.right

v = Add(1, 2)
print(v.eval())
