# TOPIC : ARRAY

from array import *

val = array('i',[3,4,5,7,9])

newVal = array(val.typecode, (i*i for i in val))

for i in range(len(newVal)):
    print(newVal[i], end=' ')

print()
print(val.itemsize)