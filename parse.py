from exp import Val, Add

def parse(s : str) :
    pos = s.find("+")
    if(pos == 0) :
        num = int(s)
        return Val(num)
    else :
        s1 = int(s[0 : pos])
        s2 = int(s[pos+1 :])
        return Add(Val(s1), Val(s2)) 

e = parse("123+234")
print(e)

# s = "123+234"
# pos = s.find("+")
# print("pos", pos)

# s1 = s[0 : pos]
# s2 = s[pos+1 :]
# print(s,s1, s2)