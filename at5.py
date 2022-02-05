n = int(input())
for i in range(n):
    frase = input().replace(".","").replace(",", "")
    diamantes = 0
    while frase.find("<>") != -1:
        frase = frase.replace("<>", "", 1)
        diamantes += 1
    print(diamantes)