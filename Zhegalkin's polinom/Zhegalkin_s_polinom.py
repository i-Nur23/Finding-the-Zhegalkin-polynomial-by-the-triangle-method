def ToBin(n):
    b = ""
    for i in range(count):
        b = str(n % 2) + b
        n = n // 2
    return b

while True:
    try:
        count = int(input("Введите кол-во символов: "))
    except :
        print ("Введите число!!!")
        continue
    if (count < 1):
        print("Введите положительное число!!!")
        continue
    break
listB = [0]*pow(2,count)
listA = [0]*pow(2,count)

string = input("Введите строку результата булевой функции: ")
res = list(string)
counter = 0
for i in range(len(res)):
    if (res[i] == '0' or res[i] == '1'):
        listB[counter] = int(res[i])
        counter += 1
        if (counter == len(listB)):
            break

resultAfterTrianagle = []
resultAfterTrianagle.append(listB[0])

bins = []
for i in range(pow(2,count)):
    bins.append(ToBin(i))

counter = 0
while (len(listA) > 1):
    listA,listB = listB,listA
    for i in range (len(listA) - 1):
        if (listA[i] + listA[i+1] == 1):
            listB[i] = 1
        else:
            listB[i] = 0
    poped = listA.pop()
    poped = listB.pop()
    resultAfterTrianagle.append(listB[0])

for i in range(pow(2,count)):
    print(bins[i] + " - " + str(resultAfterTrianagle[i]))

for i in range(len(bins)):
    if (resultAfterTrianagle[i] == 1):
        if (i == 0):
            print(1,end="")
            if i != len(bins) - 1 - resultAfterTrianagle[::-1].index(1):
                print(" + ", end="")
            else:
                print(".", end="")
            continue
        for j in range(count):
            if (bins[i][j] == "1"):
                print(f"x{j+1}",end="")
        if i != len(bins) - 1 - resultAfterTrianagle[::-1].index(1):
            print(" + ",end="")
        else:
            print(".",end="")
print(" ")