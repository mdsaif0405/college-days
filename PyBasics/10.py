# A P Q R
# A B Q R
# A B C R
# A B C D

i = 0
j = 0

v1 = ['A', 'B', 'C', 'D']
v2 = ['A', 'P', 'Q', 'R']

while i<4:
    j = 0
    while j<4:
      print(v2[j], end=' ')
      j += 1
      if i==j:
          v2[j] = v1[i]

    i += 1
    print()