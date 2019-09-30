def calc(s) :
    if(s.find("+") == -1) :
        return int(s)
    else :
        nums = map(int, s.split('+'))
        return sum(nums)

print(calc("1+2"))