t=int(input())
for _ in range(t):
    s=input()
    l=len(s)//2
    if(len(s)%2==0):
        p1=s[0:l]
        p2=s[l:]
    else:
        p1=s[0:l]
        p2=s[l+1:]
    if(sorted(p1)==sorted(p2)):
        print("YES")
    else:
        print("NO")







