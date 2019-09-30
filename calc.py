def calc(s) :
    if(len(s) == 1) :
        return int(s)
    else :
        a = s.count('+')
        b = s.count('*')
        for i in range(b) :
            int(s[s.find('*', i) - 1]) * int(s[s.find('*', i) + 1])

        return sum(nums)

print(calc("1+2"))