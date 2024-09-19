#Primeiramente, defini uma lista chamada frutas, onde contem as frutas que irei atribuir o valor
frutas= [ "acelora", "manga", "jabuticaba", "melão", "uva"]

#Criei uma variavel para armazernar o preço total das frutas.
preco_total = 0

#Portanto, foi necessário cria um loop para entradas dos preços de cada fruta.
for fruit in frutas:
    preco = float(input(f"Insira o preço da {fruit}: "))
    preco_total += preco


print()
print(f"O preço total das frutas é: R$ {preco_total:.2f}")
print()