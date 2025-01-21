s = [x**2 for x in range(19)]
#print(s)

n = [x for x in range(20) if x % 2 ==0]
#print(n)

coords = [(x, y) for x in range(3) for y in range(3)]
#print(coords)

# {ключ: значение}

a = {x:x**2 for x in range(10) if x % 2 == 0}

print(a)