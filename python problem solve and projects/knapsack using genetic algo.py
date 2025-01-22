import random
import numpy as np

file = open("input.txt", "r")

li = []
for line in file:
    li.append(line.split())
total_pl = int(li[0][0])
target = int(li[0][1])


def population(tot):
    gen_pop = []
    for i in range(10):
        x = np.random.randint(2, size=tot)
        gen_pop.append(x)
    return gen_pop


def fitness(gen_pop):
    score = []
    for it in gen_pop:
        sum = 0

        for idx, el in enumerate(it):
            if el == 1:
                sum += int(li[idx + 1][1])
        score.append(sum)
    return score


def select(score):
    temp = []
    for i in score:
        temp.append(abs(target - i))
    a = temp.index(max(temp))
    return a


def cross(x, y):
    crossing = []
    rand = random.randint(1, total_pl - 2)
    xfhalf, xlhalf, yfhalf, ylhalf = [], [], [], []

    for i in range(total_pl):
        if i <= rand:
            xfhalf.append(x[i])
            yfhalf.append(y[i])
        else:
            xlhalf.append(x[i])
            ylhalf.append(y[i])
    crossing.append(xfhalf + ylhalf)
    crossing.append(yfhalf + xlhalf)
    return crossing


def mutation(ch1, ch2):
    mutpoint = random.randint(0, total_pl - 1)
    if ch1[mutpoint] == 1:
        ch1[mutpoint] = 0
    else:
        ch1[mutpoint] = 1
    if ch2[mutpoint] == 1:
        ch2[mutpoint] = 0
    else:
        ch2[mutpoint] = 1
    return ch1, ch2


res = []

for i in range(50):
    gen_pop = population(total_pl)
    score = fitness(gen_pop)
    a = select(score)
    gen_pop.pop(a)
    ans = False

    for i in range(len(gen_pop)):
        x = random.choice(gen_pop)
        y = random.choice(gen_pop)
        child = cross(x, y)
        ch1, ch2 = child[0], child[1]
        ch1, ch2 = mutation(ch1, ch2)
        sum = 0

        for x, el in enumerate(ch1):
            if el == 1:
                sum += int(li[x + 1][1])
        if sum == target:
            res = ch1
            ans = True
            break
        sum = 0

        for x, el in enumerate(ch2):
            if el == 1:
                sum += int(li[x + 1][1])
        if sum == target:
            res = ch2
            ans = True
            break
    if ans == True:
        break


outfile = open("output.txt", "w")
if ans == False:
    print(-1)
    outfile.write(str(-1))
else:
    pl_li = []
    array = ""
    for x in range(1, len(li)):
        pl_li.append(li[x][0])
    print(pl_li)

    for el in res:
        array += str(el)
    print(array)
    outfile.write(str(pl_li) + "\n")
    outfile.write(array)

file.close()
outfile.close()
