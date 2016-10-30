#x = [1, 8, 3, 2]
#y = list(sorted(x))
#print y

x = [1, 8, 3, 2]
z = []
while x != []:
    z.append(min(x))
    x.remove(min(x))
print z