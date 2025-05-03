#🔸 Intermediários (8 a 14) – Envolvem condições dentro dos loops:

#Exercicio 8

media=0
qnt=0

while True:
    idade=int(input("Escreva a sua idade: "))
    if idade == 0:
        break 
    if idade >0:
        soma=soma+idade
        qnt=qnt+1

if qnt>0:        
  media=soma/qnt
  print(f"Média: {media}")
else: 
  print("Nenhuma quantidade de idade foi informada!")

#Exercicio 9

maior=0
while True:
    n=int(input("Insira um número: "))
    if n == 0:
        break
    if n > maior: # Se n for maior do que o valor atual de maior, então atualizamos maior com o valor de n.Isso garante que maior sempre vai guardar o maior número digitado até agora.
      maior=n

print(f"Maior: {maior}")


#Exercicio 10

soma=0
subtrair=0
while True:
    n1=int(input("Insira dois números inteiro: \n"))
    n2=int(input(""))
    
    opcao=int(input("Insira a opção: 1 - somar, 2 - subtrair, 0 - sair: "))
    
    if opcao == 0:
        print("Saiu do programa")
        break
    
    if opcao == 1:
        soma= n1+n2
        print(f"Soma dos números: {soma}")
        break
        
    if opcao == 2:
        subtrair= n1-n2
        print(f"Subtração dos múmeros: {subtrair}")
        break
        
    else: 
        print("Insira uma opção válida")
        continue
        

  

#Exercicio 11


while True:
    user=int(input("Insira a senha: "))
    
    if user == 1234:
        print("Senha correta")
        break
    else: 
        print("Senha Inválida, tente novamente")
        continue


#Exercicio 11

n = int(input("Insira um número: "))

if n <= 1:
    print("Não é primo!")

else:
    for i in range(2, n):
        if n % i == 0:  # Se n for divisível por i, não é primo
            print("Não é primo!")
            break
    else:  # Se o laço não encontrar um divisor, então é primo
        print("É primo!")


#Exercicio 13

qnt=0 #quantidade começa em 0

while True:
    n= int(input("Insira um número: "))
    if n == 0: # se n foi igual a zero, pare e pule para o proximo if 
        break
    if n % 3 == 0: #se o n for múltiplo de 3
        qnt= qnt+1 #conte mais um na quantidade
        
print(f"Quantidade de números múltiplos de 3: {qnt}") 
        
        
#Exercicio 14

for i in range(1, 51): 
  if i == 37:
    break
  print(i)