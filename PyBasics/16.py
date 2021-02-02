bits=[1,0,0,1,1,1,1,1,0,1,1,0]
stuffed=[]
count=0
for i in range(len(bits)):
    if bits[i]==1:
        count=count+1
        stuffed.append(bits[i])
    elif bits[i]!=1:
        count=0
        stuffed.append(bits[i])
    if count==5:
        stuffed.insert(i+1,0)
print(stuffed)