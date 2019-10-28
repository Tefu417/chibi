from exp import Val, Add

def parse(s: str) :
    pos = s.find("+")
    if(pos == -1) :
        num = int(s)
        return Val(num)
    else :
        s1 = s[0 : pos]
        s2 = s[pos+1 :]
        if(s1.find("+") == -1 and s2.find("+") == -1) :
            return Add(Val(int(s1)), Val(int(s2)))
        else :
            return Add(parse(s1), parse(s2))


e = parse("1+2+3")
print(e)

# s = "123+234"
# pos = s.find("+")
# print("pos", pos)

# s1 = s[0 : pos]
# s2 = s[pos+1 :]
# print(s,s1, s2)