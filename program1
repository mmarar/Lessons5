# Вариант 1 - совсем топорный, не получилось сделать обычным циклом for y in z
x = [10, 20, 30, 40]
y = len(x) # x[-1]
z = []
z1 = []

for y in range(len(x)-1, -1,-1):
    z = [x[y]]
    z1+=z

print z1

# Вариант 2 - мне понравился больше
x = [10, 20, 30, 40]
x_revers = list(reversed(x))
y = len(x) # x[-1]
z = []
z1 = []
while x != []:
    z.append(x[len(x)-1])
    x.remove(x[len(x)-1])

assert z == x_revers
print z            

# Вариант 3 с двойным срезом
x = [10, 20, 30, 40]
assert list(reversed(x)) == x[::-1]
print x[::-1]
