from exp import *

def parse(s: str) :
    posA = s.find("+")
    posM = s.rfind("*")
    posS = s.find("-")
    posD = s.rfind("/")

    if(posA == -1 and posM == -1 and posS == -1 and posD == -1) :
        num = int(s)
        return Val(num)

    elif(posM != -1) :
        s1 = s[0 : posM]
        s2 = s[posM+1 :]
    
        if(posA != -1) :
            s1 = s[0 : posA]
            s2 = s[posA+1 :]
            return Add(parse(s1), parse(s2))
        else :
            return Mul(parse(s1), parse(s2))

    elif(posM == -1 and posD == -1) :
        if(posA != -1) :
            s1 = s[0 : posA]
            s2 = s[posA+1 :]
            return Add(parse(s1), parse(s2))
        elif(posS != -1) :
            s1 = s[0 : posS]
            s2 = s[posS+1 :]
            return Sub(parse(s1), parse(s2))
            
    elif(posA != -1) :
        s1 = s[0 : posA]
        s2 = s[posA+1 :]
        return Add(parse(s1), parse(s2))

        


e = parse("1+2*3+1")
print(e)
