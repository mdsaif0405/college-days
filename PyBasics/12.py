from array import *

val = array('i', [])

n = int(input("enter size of array : "))
print("enter values")

for i in range(n):
    v = int(input())
    val.append(v)

print()
print("values in array")

for p in val:
    print(p, end=" ")

# searching

print()
print()
key = int(input("enter searching value"))

k = 0
for o in val:
    k += 1
    if o==key:
        print("found ",key)
        k = 0
if k == len(val):
    print("Not found ",key)