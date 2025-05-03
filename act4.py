class R:
    def __init__(self):
        self.v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.c=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]    
    def a(s,n):
        if n<=0: return "N/A"
        r, i="", 0
        while n:
            r+=s.c[i]*(n//s.v[i])
            n%=s.v[i]
            i+=1
        return r
n=int(input())
print(R().a(n))
