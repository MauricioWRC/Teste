def ex1():
    i = 0
    while i<=100:
        print(i)
        i+=1

#------------------------------------------
def ex2():
    i=50
    while i<=100:
        print(i)
        i+=1
def ex3():
    i=10
    while i>=0:
        print(i)
        i-=1
    print("Fogo!")

def ex4():
    numero = int(input("Digite um numero: "))
    i=1
    while i<=numero:
        print(i)
        i+=2
def ex5():
    numero = int(input("Digite um numero: "))
    i=0
    while i<=numero:
        print(i)
        i+=3
def ex6():
    numero = int(input("Digite um numero para a tabuada: "))
    i = 1
    while i<=10:
        calc = i*numero
        print(f"{numero} * {i} = {calc}")
        i+=1
def ex7():
    numero = int(input("Digite um numero para a tabuada: "))
    inicio = int(input("Digite um numero para o inicio: "))
    fim = int(input("Digite um numero para o fim: "))
    while inicio<=fim:
        calc = inicio*numero
        print(f"{numero} * {inicio} = {calc}")
        inicio+=1
def ex8():
    primeiro = int(input("Digite o primeiro numero: "))
    segundo = int(input("Digite o segundo numero: "))
    contador = 1
    calc = 0
    while contador<=primeiro: #Aqui ele vai criar um contador para fazer a soma determinadas vezes
        calc+= segundo #Realizando a soma em loop
        print(calc)
        contador+=1
def ex9():
    primeiro = int(input("Digite o primeiro numero: "))
    segundo = int(input("Digite o segundo numero: "))
    calc = primeiro
    i = 0
    while (calc-segundo)>=0:
        print(calc)
        calc-= segundo
        i+=1
    print(f"A divisão: {primeiro}/{segundo} é de {i} e com uma resto de {calc}")
def ex10():
    Primeira = str(input("Qual a soma de 4+4: A:3; B:8; C:10; D:20--> ")).lower()
    Segunda = str(input("Qual a soma de 5*4: A:20; B:8; C:10; D:15--> ")).lower()
    Terceira = str(input("Qual a soma de 4/2: A:3; B:8; C:10; D:2--> ")).lower()
    contador = 0
    if Primeira == 'b' or Segunda=='a' or Terceira=='d':
        if Primeira == 'b':#AQUI PRECISA SER IF E N ELIF PARA QUE ELE POSSA LER OS PROXIMOS
            contador+=1
        if Segunda=='a': #AQUI PRECISA SER IF E N ELIF PARA QUE ELE POSSA LER OS PROXIMOS
            contador+=1
        if Terceira=='d':
            contador+=1
        print(f"Você acertou {contador} questões")
    else:
        print('Você n acertou nenhuma. Tente novamente!')

def ex11():
    Deposito = int(input('Deposito inicial: R$:'))
    juros = int(input("Juros mensal em %: "))/100
    contador = 0
    while contador<24:
        contador+=1
        taxa = Deposito*juros
        Deposito+=taxa
        print(f"No mes {contador} o valor em conta será de R$:{Deposito:.2f}")


def ex12():
    Deposito = float(input('Deposito inicial: R$:'))
    juros = float(input("Juros mensal em %: "))/100
    contador = 0
    DepositoM = 0
    while contador<24:
        DepositoMensal = int(input('Deposito mensal R$:'))
        Deposito+=DepositoMensal
        contador+=1
        taxa = (Deposito)*juros
        Deposito+=taxa
        print(f"No mes {contador} o valor em conta será de R$:{Deposito:.2f}")

def ex13():
    divida = float(input("Valor da divida: "))
    taxa= float(input("Valor da taxa mesal em %: "))/100
    valor = float(input("Valor mensal a depositado: "))
    contador = 0
    while divida>=0:
        if valor<=0:
            print('Caloteiro safado!!')
            break
        divida-=valor
        divida+=divida*taxa
        contador+=1
        if divida<=valor:
            print(f"Você pagara por {contador} meses e no ultimo mês terá que pagar apenas R${divida:.2f} para zerar sua divida")
            break

def ex14():
    Numero = int(input('Digite um numero inteiro: '))
    contador = 0
    Soma = 0
    while Numero!= 0:
        contador+=1
        Soma+= Numero
        print("Para finalizar o processo digite o valor de 0")
        Numero = int(input('Digite um numero inteiro: '))
    aritimetica = Soma/contador
    print(f"Foram digitados {contador} numero, sua soma foi de {Numero} e a média aritimetica de {aritimetica}")

def ex15():
    codigo = input('''Produtos
          Código 1 - Proço R$ 0,50
          Código 2 - Proço R$ 1,00
          Código 4 - Proço R$ 4,00
          Código 5 - Proço R$ 7,00
          Código 9 - Proço R$ 8,00
          Digite 0 para finalizar a compra
        Codigo: ''')
    contador = 0
    valor =0
    while codigo!="0":
        if codigo == "1":
            valor+=0.5

        if codigo == "2":
            valor+=1

        if codigo=="4":
            valor+=4

        if codigo=="5":
            valor+=7

        if codigo=="9":
            valor+=8
        print(f"Valor total: {valor}")
        if codigo!='1' and codigo!='2' and codigo!='4' and codigo!= '5' and codigo!='9' and codigo!='0':
            print('Codigo invalido')
            contador-=1
        if codigo == '0':
            break
        codigo = input("Codigo: ")
        contador+=1
    print(f'''Quantidades de itens: {contador} 
Valor total: {valor}''')


def ex16():
    valor = int(input("Insira o valor: R$ "))
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    while valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
        print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1''')
        valor = int(input("Insira o valor: R$ "))
def ex17():
    valor = 0
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    if valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
    print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1''')

def ex18():
    valor = int(input("Insira o valor: R$ "))
    notas100=0;nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    if valor>0:
        while valor>=100:
            notas100+=1
            valor-=100
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
    print(f'''Foram utilizados:
{notas100} notas de 100
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1''')

def ex19():
    valor = float(input("Insira o valor: R$ "))
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    moedas1 =0;moedas2 =0;moedas5 =0;moedas10 =0;moedas50=0
    if valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
        while valor>=0.5:
            moedas50+=1
            valor-=0.49
        while valor>=0.1:
            moedas10+=1
            valor-=0.1
        while valor>=0.05:
            moedas5+=1
            valor-=0.05
        while valor>=0.02:
            moedas2+=1
            valor-=0.02
        while valor>=0.01:
            moedas1+=1
            valor-=0.01

    print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1
{moedas50} moedas de 50
{moedas10} moedas de 10
{moedas5} moedas de 5
{moedas2} moedas de 2
{moedas1} moedas de 1
''')

def ex20():
    valor = float(input("Insira o valor: R$ "))
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    moedas1 =0;moedas2 =0;moedas5 =0;moedas10 =0;moedas50=0
    if valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
        while valor>=0.5:
            moedas50+=1
            valor-=0.49
        while valor>=0.1:
            moedas10+=1
            valor-=0.1
        while valor>=0.05:
            moedas5+=1
            valor-=0.05
        while valor>=0.02:
            moedas2+=1
            valor-=0.02
        while valor>=0.01:
            moedas1+=1
            valor-=0.01

    print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1
{moedas50} moedas de 50
{moedas10} moedas de 10
{moedas5} moedas de 5
{moedas2} moedas de 2
{moedas1} moedas de 1
''')
    if valor<0.01 and valor!=0:
        print(f'Valor abaixo do esperado: {valor}')

def ex21():
    return ex16()

def ex22():
    loop = True
    while loop == True:
        menu = str(input('''MENU
ADIÇÃO          --> [1]
SUBTRAÇÃO       --> [2]
DIVISÃO         --> [3]                
MULTIPLICAÇÃO   --> [4]                  
SAIR            --> [5]        

OPÇÃO DESEJADA: '''))
        if menu == '1':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor a somar: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} + '))
                resultado += Numero1
            print(f"O valor das somas foi de {resultado}")
        if menu == '2':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor a subtrair: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} - '))
                resultado -= Numero1
            print(f"O valor das subtrações foi de {resultado}")
        if menu == '3':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor dividir: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} / '))
                resultado /= Numero1
            print(f"O valor das divisões foi de {resultado}")
        if menu == '4':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor multiplicar: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} * '))
                resultado *= Numero1
            print(f"O valor das somas foi de {resultado}")
        if menu == '5':
            loop = False

def ex23():
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    numero = int(input("Digite um número: "))
    if eh_primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

def ex24():

    """def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    numero = int(input("Digite uma quantidade: "))
    contador = 3  # Começa do 3 porque é o primeiro número primo ímpar após 2
    verificador = [False, False, False]  # Lista de verificação de 3 primos
    mod = 0  # Índice para controlar as alterações na lista

    while verificador != [True, True, True]:
        if contador >= numero:
            print("Contador ultrapassou o número dado.")
            break
        if eh_primo(contador):
            verificador[mod] = True  # Corrigido para fazer a atribuição correta
            print(f"{contador} é primo.")
            mod += 1  # Muda para o próximo índice da lista de verificação
            if mod == len(verificador):
                break  # Sai do loop quando os 3 valores da lista foram alterados para True
        contador += 2  # Verifica apenas números ímpares a partir de 3 (primos ímpares)"""
    
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    numero = int(input("Digite uma quantidade: "))
    contador = 3  # Começa do 3 porque é o primeiro número primo ímpar após 2
    verificador = [False]*numero  # Lista de verificação de 3 primos
    mod = 0  # Índice para controlar as alterações na lista
    while verificador != [True]*numero:
        if eh_primo(contador):
            verificador[mod] = True  # Corrigido para fazer a atribuição correta
            print(f"{contador} é primo.")
            mod += 1  # Muda para o próximo índice da lista de verificação
            if mod == len(verificador):
                break  # Sai do loop quando os 3 valores da lista foram alterados para True
        contador += 2  # Verifica apenas números ímpares a partir de 3 (primos ímpares)
def ex25():
    n = int(input("Digite um número para descobrir sua raiz quadrada: "))
    b = 2
    tolerancia = 0.001
    while True:
        p = (b + (n / b)) / 2
        quadrado_p = p * p
        if abs(n - quadrado_p) < tolerancia:
            break
        b = p
    print(f"A raiz quadrada aproximada de {n} é {p:.3f}")

def ex26():
    Dividendo = int(input("Dividendo: "))
    backup = Dividendo
    Divisor = int(input("Divisor: "))
    contador=0
    while Dividendo> Divisor:
        Dividendo-=Divisor
        contador+=1
    print(f"A Divisão de {backup} por {Divisor} = {contador} com resto de {Dividendo}")

def ex27():
    funciona = True
    while funciona == True:
        print("Digite 0 para sair")
        numero = int(input("Digite o numero para ver se é palíndromo: "))
        digitos = [int(digito) for digito in str(numero)] #Precisa tranformar em string para depois colocar em numero para ficar certinho na lista
        contador_Inicio = 0
        contador_Fim = len(digitos)-1 #Vai ler a quantidade de itens na lista
        verificador = True
        if numero == 0:
            break
        while contador_Inicio != contador_Fim:
            if digitos[contador_Inicio] != digitos[contador_Fim]:
                print(f"O numero {numero} não é palíndromo")
                verificador = False
                break
            contador_Inicio+=1
            contador_Fim-=1
        if verificador == True:
            print(f"O numero {numero} é palindromo")



opções = [None,ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,
              ex10,ex11,ex12,ex13,ex14,ex15,ex16,ex17,ex18,ex19,
              ex20,ex21,ex22,ex23,ex24,ex25,ex26,ex27]
funciona= True
while funciona == True:
    escolha = int(input('''
----------//-------------//-------------//------------//----------// ----
Escolha um exercicio para ver a funcionalidade
exercicios disponiveis do 1 ao 22 e digite 0 para sair,
apenas digitar o numero do exercicio que funcionará no seu termianl, tmj
                    
Numero do exercicio: '''))
    print("----------//-------------//-------------//------------//----------// ----")
    if escolha == 0:
        funciona=False
        break
    if escolha!=0:
        opções[escolha]()
    else:
        print("Escolha invalida.")