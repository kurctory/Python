def sortByAlphabet(inputStr):
        return inputStr[0] # Ключом является первый символ в каждой строке, сортируем по нему

data = []
with open("a.txt") as f:
    for lineA in f:
        data.append(lineA.strip())
        
with open("b.txt", "r") as f:
    for lineB in f:
        data.append(lineB.strip())

data.sort(key = sortByAlphabet)
print(data)

with open("c.txt", "w") as f:
    for line in data:
        f.write(line)
        f.write(" ")

