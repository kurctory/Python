def sort(Str):
        return Str[0] # Ключом является первый символ в каждой строке, сортируем по нему

data = []
with open("a.txt") as f:
    for line in f:
        data.append(line.strip())
        
with open("b.txt", "r") as f:
    for line in f:
        data.append(line.strip())

data.sort(key = sort)
print(data)

with open("c.txt", "w") as f:
    for line in data:
        f.write(line)
        f.write(" ")

