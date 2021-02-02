# function prototype


def cal(a, b):
    return a+b, a-b, a*b, a/b


x, y, z, d = cal(int(input('value1 : ')),
                 int(input('value2 : ')))

print("sum = %d" %x,
      "sub = %d" %y,
      "product = %d" %z,
      "div = %.2f" %d)
