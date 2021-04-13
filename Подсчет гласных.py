# 2. Подсчет гласных
# Разин ПИ223
string = str(input("Введите предложение:"))
countA = 0
countO = 0
countU = 0
countI = 0
countE = 0
countY = 0
for a in string:
    if a == "a" or a == "A":
        countA+=1
print("кол-во a =", countA)
for o in string:
    if o == "o" or o == "O":
        countO+=1
print("кол-во o =", countO)
for u in string:
    if u == "u" or u == "U":
        countU+=1
print("кол-во u =", countO)
for i in string:
    if i == "i" or i == "I":
        countI+=1
print("кол-во i =", countI)
for e in string:
    if e == "e" or e == "E":
        countE+=1
print("кол-во e =", countE)
for y in string:
    if y == "y" or y=="Y":
        countY+=1
print("кол-во y =", countY)
print("a", countA,",", "o", countO,",", "u", countU,",", "i", countI,",", "e", countE,",", "y", countY)

