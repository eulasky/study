ch = [0] + list(map(int, input().split()))

newPizza = 1
oven = [0] * N

while oven:
    pizza = oven.pop(0)
    ch[pizza] //= 2
    if ch[pizza] == 0:
        if newPizza <= M:
            oven.append(newPizza)
            newPizza += 1
    else:
        oven.append(pizza)
