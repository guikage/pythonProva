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

        m2 = int(input("Digite a area a ser pintada (em metros quadrados): "))
        litros = m2/3
        latas = int(litros/18)
        if litros/18 > int(litros/18):
            latas+=1
        preco = latas*80

        print("Voce devera comprar %d latas, isso custara R$%d" % (latas, preco))
    
    def ex17():
        print("\n--------EXERCICIO 17--------\n")

        m2 = int(input("Digite a area a ser pintada (em metros quadrados): "))
        litros = m2/3
        
        latas = ((litros/18)+(0.1*litros/18))
        if (litros/18)+(0.1*litros/18) > int((litros/18)+(0.1*litros/18)):
            latasint=int(latas)+1
        else:
            latasint=int(latas)
        
        galoesint = int((litros/3.6)+(0.1*litros/3.6))
        if (litros/3.6)+(0.1*litros/3.6) > int((litros/3.6)+(0.1*litros/3.6)):
            galoesint+=1

        if latas<latasint:
            litros2 = latasint-(litros/18)
            galoes2 = int((litros2/3.6)+(0.1*litros2/3.6))
            if (litros2/3.6)+(0.1*litros/3.6) > int((litros/3.6)+(0.1*litros/3.6)):
                galoes2+=1
        

        print(latas)
        print(latasint)
        print(galoesint)
        print((int(latas), galoes2))



    














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
    elif seletor == 16:
        ex16()
    elif seletor == 17:
        ex17()


    else:
        print("DIGITOU ERRADO ANIMAL")

if __name__ == '__main__':
    main()
