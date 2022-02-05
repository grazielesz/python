def main():
    data = input("insira sua data de nascimento (no formato dd/mm/aaaa e sem barras): ")
    dict = {'01':'janeiro', '02':'fevereiro', '03':'março', '04':'abril', '05':'maio', '06':'junho', '07':'julho', '08':'agosto', '09':'setembro', '10':'outubro', '11':'novembro', '12':'dezembro'}

    if int(data[2:4]) > 12:
        print("\n>> mês inválido <<")
    else:
        print("\n" + data[0:2], "de", dict[data[2:4]], "de", data[4::])

main()
		
