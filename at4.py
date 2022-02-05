frase = input("insira uma frase: ")
while (frase != "*"):
    letra = frase[0]
    tautograma = "Y"
    for palavra in frase.split(" "):
        if palavra[0].lower() != letra[0].lower():
            tautograma = "N"
            break
    print(tautograma)
    tautograma = "Y"
    frase = input("insira uma frase: ")