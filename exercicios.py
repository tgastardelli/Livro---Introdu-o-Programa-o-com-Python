print(10 + 20 * 30)
print(9 ** 2 / 30)
print(10%3*(10**2)+1-10*4/2)
print('Thiago')
a = 3
b = 5
print(2*a*3*b)
var1 = 1
var2 = 2
var3 = 3
print(var1 + var2 + var3)
salario = 750
aumento = 15
print(salario + (salario * aumento / 100))
print(3*0.1)
print(0b10)
print(0x10)
print(0o10)
salario = 1500
print(salario > 1200)

materia1 = 7
materia2 = 9
materia3 = 4
media = ((materia1 + materia2 + materia3) / 3)
if media > 7:
    print('aluno aprovado')
else:
    print('aluno reprovado')


materia1 = 7
materia2 = 9
materia3 = 4
print(materia1 >= 7 and materia2 >= 7 and materia3 >=7)

print(len('a'))

x = 10
print('João tem %d anos' %x)
#% indica a composição da string anterior com o conteúdo da variável 'x'
#%d representa a marcação de posição de um valor inteiro
login = 1
print('O usuário chamado foi: %s' %login)
#%s representa a marcação de posição de uma string
nome = 'João'
idade = 22
grana = 51.54
print('%s tem %d anos e apenas R$%2.2f no bolso' % ("João", 22, 54.3165))
#%f representa a marcação de número decimais | 2 valores entre % e f onde o primeiro 
# indica o total em caracteres e o se gundo, o número de casas decimais
#% indiciar a composição da string anterior com o conteúdo das variáveis
idade = 22
print("%d" % idade)
#format em vez de % (forma mais moderna e prática, 
# não precisa especificar os tipos de % usando {})
nome = "João"
idade = 22
grana = 51.54
print("{} tem {} anos e R${} no bolso." .format(nome,idade,grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso." .format(nome,idade,grana))
# 3ª forma usando f-string (escrevemos a letra f antes das aspas e o nome da variável entre
# chaves {})
nome = "João"
idade = 22
grana = 51.34
print(f"{nome} tem {idade} anos e R${grana} no bolso.")
print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso.")
#fatiamento de strings
s = "ABCDEFGHI"
print(s[0:2])
print(s[1:2])
#3.7 Entrada de Dados
# input é utilizada para solicitar dados do usuário, sempre retorndando como string
x = input("Digite um número: ")
print(x)

nome = input("Digite seu nome: ")
print(f"Você digitou {nome}.")
print(f"Olá, {nome}!")

#3.7.1 Conversão da Entrada de Dados
#int (número inteiro) float(ponto flutuante; número decimal)
anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bônus de R$ {bonus:5.2f}")

#Exercício 3.7 page 72
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(f"A soma dos dois número é de: {num1 + num2}")

#Exercício 3.8
metro = float(input("Digite um número em metros: "))
mil = metro * 1000
print(f"O valor de {metro} metros são {mil} milímetros")

#Exercício 3.9
dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

resultado1 = dias * 24 * 60 * 60
resultado2 = horas * 60 * 60
resultado3 = minutos * 60
total = resultado1 + resultado2 + resultado3
print(f"O total em segundos é de: {total} segundos.")

dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)

#exercício 3.10
salario = float(input("Digite seu salário: "))
aumento = float(input("Qual a porcentagem do aumento? "))
aumento1 = salario * aumento / 100
novo_salario = aumento1 + salario
print(f"Aumento de {aumento1}")
print(f"Novo salário de R${novo_salario:5.2f}")

#exercício 3.11
preco = float(input("Preço da mercadoria: R$"))
desconto = float(input("Percentual de desconto: "))
valor_desconto = preco * desconto / 100
apagar = preco - valor_desconto
print(f"Valor do desconto R${valor_desconto:5.2f}")
print(f"Valor à pagar R${apagar:5.2f}")

#exercício 3.12
distancia = float(input("Quantos km à percorrer? "))
velocidade = float(input("Em qual velocidade media p/hr? "))
tempo = distancia / velocidade * 60
print(f"O tempo dessa viagem é de {tempo:.0f} minutos")

distância = float(input("Digite a distância em km:"))
velocidade_média = float(input("Digite a velocidade média em km/h:"))
tempo = distância / velocidade_média
print("O tempo estimado é de %5.2f horas" % tempo)
# Opcional: imprimir o tempo em horas, minutos e segundos
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)
print("%05d:%02d:%02d" % (horas, minutos, segundos))

#exercício 3.13
temp1 = float(input("Temperatura em °C "))
temp2 = (9 * temp1 / 5) + 32
print(f"°C {temp1} equivale a °F {temp2}")

#exercício 3.14
km_carro = float(input("Quantos KM percorridos? "))
dias_carro = int(input("Carro alugado por quantos dias? "))
apagar = (60 * dias_carro) + (0.15 * km_carro)
print(f"O preço a pagar será de R${apagar:7.2f}")


#exercício 3.15
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já 
# fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro e 
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
cigarros_dia = int(input("Cigarros por dia: "))
anos_fumado = float(input("Quantos anos fumando? "))
reducao_minutos = anos_fumado * 365 * cigarros_dia * 10
reducao_dias = reducao_minutos / (24 * 60)
print(f"Redução do tempo de vida em dias: {reducao_dias:5.2f}")

#exercício 4.2
velocidade_carro = float(input("Qual a velocidade do carro em KM/H? "))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 5
    print(f"Usuário multado em R$ {multa:7.2f}")
if velocidade_carro <= 80:
    print("Velocidade permitida")

#exercício 4.3
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))
if num1 > num2 and num1 > num3:
    print(f"Maior número: {num1}")
if num2 > num1 and num2 > num3:
    print(f"Maior número: {num2}")
if num3 > num1 and num3 > num2:
    print(f"Maior número: {num3}")
if num1 < num2 and num1 < num3:
    print(f"Menor número: {num1}")
if num2 < num1 and num2 < num3:
    print(f"Menor número: {num2}")
if num3 < num1 and num3 < num2:
    print(f"Menor número: {num3}")



a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")

#exercício 4.4
salario = float(input("Qual o salário? "))
aumento = salario
if salario > 1250:
    aumento = salario * 0.10
    print(f"Aumento de 10%: R${aumento:5.2f}")
aumento = salario
if salario <= 1250:
    aumento = salario * 0.15
    print(f"Aumento de 15%: R${aumento:5.2f}")
#####################
salário = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salário > 1250:
    pc_aumento = 0.10
aumento = salário * pc_aumento
print(f"Seu aumento será de: R$ {aumento:7.2f}")
#####################
#exercício 4.6
km = float(input("Quantos KM deseja percorrer? "))
if km <= 250:
    preco_passagem = km * 0.50
else:
    preco_passagem = km * 0.45
print(f"Preço passagem: R$ {preco_passagem:7.2f}")

# elif: elif substitui um par else/if, mas sem criar outro nível de estrutura,
# evitando deslocamentos descenessários à direita.

#exercício 4.8
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operador = str(input("Qual operação deseja realizar? +, -, *, /: "))
if operador == "+":
    conta = num1 + num2
elif operador == "-":
    conta = num1 - num2
elif operador == "*":
    conta = num1 * num2
elif operador == "/":
    conta = num1 / num2
else:
    print("Operação inválida!")
print(f"Resultado da operação: {conta}")

#exercício 4.9
# empréstimo bancário para compra de uma casa
valor_casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos_apagar = float(input("Quantos anos à pagar? "))
prestacao_mensal = valor_casa / (anos_apagar * 12)

if prestacao_mensal > (salario * 0.30):
    print("Empréstimo recusado!")
else:
    print(f"Empréstimo aprovado! Valor mensal à pagar: R${prestacao_mensal:.2f}")

# exercício 4.10
kwh = int(input("Qual a quantidade de kWh consumida? "))
instalacao = str(input("Qual o tipo de instalão? R, I, C: "  ))
if instalacao == "R" and kwh <= 500:
    apagar = kwh * 0.40
elif instalacao == "R" and kwh > 500:
    apagar = kwh * 0.65
elif instalacao == "C" and kwh <= 1000:
    apagar = kwh * 0.55
elif instalacao == "C" and kwh > 1000:
    apagar = kwh * 0.60
elif instalacao == "I" and kwh <= 5000:
    apagar = kwh * 0.55
elif instalacao == "I" and kwh > 5000:
    apagar = kwh * 0.60
print(f"Preço a pagar: R$ {apagar:.2f}")

#Repetições...
# Uma das estruturas de repetições do python é o WHILE, que repete o bloco
# enquanto a condição for verdadeira
x = 1
while x <= 100:
    print(x)
    x = x + 1

x = 50
while x <=100:
    print(x)
    x = x + 1

contagem = 10
while contagem >= 0:
    print(f"{contagem}...")
    contagem = contagem - 1
print("Fogo!")
    
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
    print(x)
    x = x + 2

fim = int(input("Digite o último número a imprimir: "))
x = 0
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1

fim = 30
x = 3
while x <= fim:
    print(x)
    x = x + 3
    
n = int(input("Tabuada de: "))
x = 1
while x <= 10:
    print(n + x)
    x = x + 1

# exercício 5.6
n = int(input("Tabuada de multiplicação; número: "))
resultado = 1
while resultado <= n:
    resultado = resultado * 2
    print(f"{resultado}x2 = {resultado}")

n = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x + 1

#Exercício 5.7
tabuada = int(input("Tabuada de: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
while inicio <= fim:
    print(f"{tabuada} x {inicio} = { tabuada * inicio}")
    inicio = inicio + 1

#Exercício 5.8
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
while num1 <= num2:
    x = num1 + num1
    print()





















































