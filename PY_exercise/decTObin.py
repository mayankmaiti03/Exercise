def dec_to_bin(n):
    b=""
    if n==0:
        return "0"
    while n>0:
        r=n%2
        b=str(r)+b
        n=n//2
    return b

n=4
print(dec_to_bin(n))

