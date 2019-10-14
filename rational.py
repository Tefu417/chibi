import math

class Q(object) :
    def __init__(self, a, b = 1) :
        # この時点ではselfは空
        # なんの変数名が与えられているか分からないから 自分自身 = self
        # 他言語では self の代わりに this
        # Q(a, b)のa, bをself.a, self.bと名付ける(初期化)
        # bが省略されたときb = 1
        gcd = math.gcd(a, b)
        self.a = a // gcd
        self.b = b // gcd
        
    def __repr__(self) :
        if(self.b == 1) :
            return str(self.a)
        else :
            return f'{self.a}/{self.b}'

    def __add__(self, q) :  #self = q1, q = q2
        if(isinstance(q, int)) :
            q = Q(q, 1)
        a = self.a * q.b + q.a * self.b
        b = self.b * q.b
        return Q(a, b)

    def __sub__(self, q) :
        if(isinstance(q, int)) :
            q = Q(q, 1)
        a = self.a * q.b - q.a * self.b
        b = self.b * q.b
        return Q(a, b)

    def __mul__(self, q) :
        if(isinstance(q, int)) :
            q = Q(q, 1)
        a = self.a * q.a
        b = self.b * q.b
        return Q(a, b)

    def __truediv__(self, q) :
        if(isinstance(q, int)) :
            q = Q(q, 1)
        a = self.a * q.b
        b = self.b * q.a
        return Q(a, b)

q1 = Q(2, 4)
# クラスでコンストラクタを呼んでいる
# __init__ が呼ばれる
# q1.a => 2
# q1.b => 4
# ↑　ここでは自分で名前を付けている（勝手には名前は付けられない）
q2 = Q(1, 3)

print(q1)
print(q1 + q2)
print(q1 - q2)
print(q1 * q2)
print(q1 / q2)

q = Q(1, 2)
print(q / 2)