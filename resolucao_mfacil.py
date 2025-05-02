# Modo Fáceis (1 a 7) – Ideal para treinar lógica e sintaxe básica:

#Exercício 1
i=0
while i<=10: 
    print(i)
    i=i+1
    
#Exercício 2
for i in range(10,0,-1):
    print(i)
#print(list(10,0,-1))


#Exercício 3

print("Tabuada de 1 a 10")
numero=int(input("Insira o número que queira a tabuada: "))
print(f"Tabuada do {numero}")

for i in range (1,11):
  multi= numero * i
  print(f"{numero}x{i}={multi}")

#Exercício 4

soma=0
print("Insira números e digite 0 quando deseja somar!")
while True:
    numero=int(input("Digite um número: "))
    if numero == 0:
        break
    soma=numero+numero
print(f"Somatória de todos os números:{soma}")


#Exercício 5

qnt=0
while True:
    n=int(input("Insira números neg e positivos: "))
    if n==0:
        break
    if n>=0:
        qnt=qnt+1
print(f"Quantidade de numeros positivos:{qnt}")

#Exercício 6

for i in range(0,101,2):
    print(i)

#Exercício 7

for i in range(0, 21):
    if i % 4 == 0:
        continue
    print(i)














