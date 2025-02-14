def hcf2(a,b):
    if a>b:
        s=b
    else:
        s=a
    for i in range(1,s+1):
        if((a%i==0) and (b%i==0)):
            h=i
    return h

a=10000000000000000000000000000
b=2184654718649575
print(hcf2(a, b))