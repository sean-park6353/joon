# 다이얼

n = input()

arr = []
for i in range(len(n)):
    if n[i] == "A" or n[i] == "B" or n[i] == "C":
        arr.append(2)
    elif n[i] == "D" or n[i] == "E" or n[i] == "F":
        arr.append(3)
    elif n[i] == "G" or n[i] == "H" or n[i] == "I":
        arr.append(4)
    elif n[i] == "J" or n[i] == "K" or n[i] == "L":
        arr.append(5)
    elif n[i] == "M" or n[i] == "N" or n[i] == "O":
        arr.append(6)
    elif n[i] == "P" or n[i] == "Q" or n[i] == "R" or n[i] == "S":
        arr.append(7)
    elif n[i] == "T" or n[i] == "U" or n[i] == "V":
        arr.append(8)
    elif n[i] == "W" or n[i] == "X" or n[i] == "Y" or n[i] == "Z":
        arr.append(9)

print(sum(arr)+len(arr))
