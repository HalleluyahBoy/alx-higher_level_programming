from calculator_1 import add, sub, mul, div

a = 10
b = 5

result_a = add(a, b)
print("{0} + {1} = {2}".format(a, b, result_a))

result_b = sub(a, b)
print("{0} - {1} = {2}".format(a, b, result_b))

result_c = mul(a, b)
print("{0} * {1} = {2}".format(a, b, result_c))

result_d = div(a, b)
print("{0} / {1} = {2}".format(a, b, result_d))
