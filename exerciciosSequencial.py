def main():
    def ex11():
        print("\n--------EXERCICIO 11--------\n")

        n1 = int(input("Digite um numero inteiro: "))
        n2 = int(input("Digite outro numero inteiro: "))
        n3 = float(input("Digite um numero real: "))

        print((n1*2)*(n2/2))
        print((n1*3)+n3)
        print(n3**3)

    def ex12():
        print("\n--------EXERCICIO 12--------\n")   
       
        altura = float(input("Digite sua altura (em metros, yankee fedido): "))
        print("Peso ideal:", (72.7*altura)-58)
        
    def ex13():
        print("\n--------EXERCICIO 13--------\n")

        altura = float(input("Digite sua altura (em m): "))
        genero = input("Digite M se for do sexo masculino e F se for do sexo feminino: ")

        if genero.lower() == 'm':
            ideal = (72.7*altura)-58
            print("Peso ideal: %.3f" % ideal)
        elif genero.lower() == 'f':
            ideal = (62.1*altura)-44.7
            print("Peso ideal: %.3f" % ideal)
        else:
            print("Esse genero nao existe")

    def ex14():
        print("\n--------EXERCICIO 14--------\n")

        peso = float(input("Digite o peso dos peixes em kg: "))

        excesso = peso-50
        multa = excesso*4

        print("Excesso: %.2f" % excesso)
        if multa > 0:
            print("Multa: %.2f" % multa)
        else:
            print("Nao tem multa")
    
    def ex15():
        print("\n--------EXERCICIO 15--------\n")

        reais = float(input("Quantos reais voce ganha por hora? "))
        horas = float(input("Quantas horas voce trabalhou no mes? "))

        sBruto = reais*horas
        ir = sBruto * (11/100)
        inss = sBruto * (8/100)
        sindicato = sBruto * (5/100)
        sLiquido = sBruto - ir - inss - sindicato

        print("""\n+ Salario Bruto: R$%.2f\n- IR (11): R$%.2f\n- INSS (8): R$%.2f\n- Sindicato (5): R$%.2f\n= Salario Liquido: R$%.2f""" % (sBruto, ir, inss, sindicato, sLiquido))

    def ex16():
        print("\n--------EXERCICIO 16--------\n")
    














    seletor = int(input("Digite o numero do exercicio: "))
    if seletor == 11:
        ex11()
    elif seletor == 12:
        ex12()
    elif seletor == 13:
        ex13()
    elif seletor == 14:
        ex14()
    elif seletor == 15:
        ex15()


    else:
        print("DIGITOU ERRADO ANIMAL")

if __name__ == '__main__':
    main()
