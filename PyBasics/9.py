# [ A P Q R ]
# [ A B Q R ]
# [ A B C R ]
# [ A B C D ]

a = 0
b = 0

v1 = ['A', 'B', 'C', 'D']
v2 = ['A', 'P', 'Q', 'R']

for p in v1:
     for l in v2:
        b += 1
        print(l, end=' ' )
        if a==b:
          v2[a] = v1[b]
     a += 1
     b = 0
     print()