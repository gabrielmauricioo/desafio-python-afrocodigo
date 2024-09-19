# irei pedir ao usuário que me diga o preço do produto e o percentual que será aplicado.
valor_do_produto = int(input("Olá, digite por favor o preço do produto: "))
print()
percentual_aplicado = int(input("Agora, diga, quantos porcentos de desconto, deseja: "))
print()

# Peguei, o “valor do percentual” e dividi por 100. Em seguida, irei peguei o resultado desta divisão e multipliquei pelo “valor do produto “
divisao = percentual_aplicado / 100
multiplicacao = divisao * valor_do_produto

# Para finalizar, peguei o resultado final desta multiplicação e diminui pelo “valor do produto”, tendo como resposta o desconto aplicado.
resultado = valor_do_produto - multiplicacao
print(f"O preço com desconto é R$ {resultado:.2f}")