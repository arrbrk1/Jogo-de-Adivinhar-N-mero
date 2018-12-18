from random import randint

j = randint(0, 10)
counter = 1
while True:
  i = int(input("Digite um número de 1 a 10: "))
  if counter == 20:
    print("Você excedeu o número de tentativas!")
  if i <= 10:
      if i != j:
          print("Tente de novo!")
          counter += 1
      else:
          print("Você acertou! Parabéns!")
          print("Foram {} tentativas!".format(counter))
          break
  else:
      print("Você digitou um número acima de 10!")
      break
