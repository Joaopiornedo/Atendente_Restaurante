from PIL import Image

imagem = Image.open('Pastel.png')

print("Olá, sou o SR Pastel e irei te ajudar com seu pedido! Vamos fazer um breve Cadastro: ")

nome = str(input("Digite seu nome: ")).title()
endereco = str(input("Digite seu endereço : ")).title()

print(f"Certo {nome}, irei te mostrar o cardápio:")

imagem.show()

carrinho =[]

sabores_pasteis = [
    {"1": "Pastel Carne", "valor": 10},
    {"2": "Pastel Queijo", "valor": 10},
    {"3": "Pastel Pizza", "valor": 10},
    {"4": "Pastel Frango", "valor": 10},
    {"5": "Pastel Bacon", "valor": 12},
    {"6": "Pastel Calabresa", "valor": 10},
    {"7": "Pastel Chocolate ao leite", "valor": 15},
    {"8": "Pastel Leite em pó", "valor": 18},
    {"9": "Pastel Morango c/ Chocolate", "valor": 25},
    {"10": "Pastel Chocolate Branco", "valor": 25},
    {"11": "Pastel Banana c/ Canela", "valor": 25},
    {"12": "Pastel Romeu e Julieta", "valor": 25},
    {"13": "Pastel 2 Sabores", "valor": 15},
    {"14": "Pastel 3 Sabores", "valor": 18},
    {"15": "Pastel 4 Sabores", "valor": 25},
    {"16": "Pastelão", "valor": 25},
    ]

while True:
    resposta_cliente = int(input("Escolha o número correspondente ao sabor desejado: "))
    if resposta_cliente == 1:
        quantidade_carne = int(input("Escolha a quantidade de Pastel de Carne: "))
        carrinho.append(f"Pastel de Carne {quantidade_carne} unidades, Valor: {quantidade_carne * 10} Reais")  
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 2:
        quantidade_queijo = int(input("Escolha a quantidade de Pastel de Queijo: "))
        carrinho.append(f"Pastel de Queijo {quantidade_queijo} unidades, Valor: {quantidade_queijo * 10} Reais") 
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 3:
        quantidade_pizza = int(input("Escolha a quantidade de Pastel de Pizza: "))
        carrinho.append(f"Pastel de Pizza {quantidade_pizza} unidades, Valor: {quantidade_pizza * 10} Reais") 
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 4:
        quantidade_frango = int(input("Escolha a quantidade de Pastel de Frango: "))
        carrinho.append(f"Pastel de Frango {quantidade_frango} unidades, Valor: {quantidade_frango * 10} Reais") 
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 5:
        quantidade_bacon = int(input("Escolha a quantidade de Pastel de Bacon: "))
        carrinho.append(f"Pastel de Bacon {quantidade_bacon} unidades, Valor: {quantidade_bacon * 10} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break 

    if resposta_cliente == 6:
        quantidade_calabresa = int(input("Escolha a quantidade de Pastel de Calabresa: "))
        carrinho.append(f"Pastel de Calabresa {quantidade_calabresa} unidades, Valor: {quantidade_calabresa * 10} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break 

    if resposta_cliente == 7:
        quantidade_chocolate_ao_leite = int(input("Escolha a quantidade de Pastel de Chocolate ao Leite: "))
        carrinho.append(f"Pastel de Chocolate ao Leite {quantidade_chocolate_ao_leite} unidades, Valor: {quantidade_chocolate_ao_leite * 15} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break 

    if resposta_cliente == 8:
        quantidade_leite_em_po = int(input("Escolha a quantidade de Pastel de Leite em pó: "))
        carrinho.append(f"Pastel de Leite em pó {quantidade_leite_em_po} unidades, Valor: {quantidade_leite_em_po * 18} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 9:
        quantidade_morango_com_chocolate = int(input("Escolha a quantidade de Pastel de Morango c/ Chocolate: "))
        carrinho.append(f"Pastel de Morango c/ Chocolate {quantidade_morango_com_chocolate} unidades, Valor: {quantidade_morango_com_chocolate * 25} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break 

    if resposta_cliente == 10:
        quantidade_chocolate_branco = int(input("Escolha a quantidade de Pastel de Chocolate Branco: "))
        carrinho.append(f"Pastel de Chocolate Branco {quantidade_chocolate_branco} unidades, Valor: {quantidade_chocolate_branco * 25} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break 
    
    if resposta_cliente == 11:
        quantidade_banana_com_canela = int(input("Escolha a quantidade de Pastel de Banana c/ Canela: "))
        carrinho.append(f"Pastel de Banana c/ Canela {quantidade_banana_com_canela} unidades, Valor: {quantidade_banana_com_canela * 25} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break
    
    if resposta_cliente == 12:
        quantidade_romeu_e_julieta = int(input("Escolha a quantidade de Pastel de Romeu e Julieta: "))
        carrinho.append(f"Pastel de Romeu e Julieta {quantidade_romeu_e_julieta} unidades, Valor: {quantidade_romeu_e_julieta * 25} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break
    
    if resposta_cliente == 13:
        quantidade_2_sabores = int(input("Escolha a quantidade de Pastel 2 Sabores: "))
        carrinho.append(f"Pastel 2 Sabores {quantidade_2_sabores} unidades, Valor: {quantidade_2_sabores * 15} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break
    
    if resposta_cliente == 14:
        quantidade_3_sabores = int(input("Escolha a quantidade de Pastel 3 Sabores: "))
        carrinho.append(f"Pastel 3 Sabores {quantidade_3_sabores} unidades, Valor: {quantidade_3_sabores * 18} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 15:
        quantidade_4_sabores = int(input("Escolha a quantidade de Pastel 4 Sabores: "))
        carrinho.append(f"Pastel 4 Sabores {quantidade_4_sabores} unidades, Valor: {quantidade_4_sabores * 25} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break

    if resposta_cliente == 16:

        quantidade_pastelao = int(input("Escolha a quantidade de Pastel de Pastelão: "))
        carrinho.append(f"Pastel de Pastelão {quantidade_pastelao} unidades, Valor: {quantidade_pastelao * 25} Reais")
        continuar_pedido = str(input("Deseja adicionar mais algum produto? (s)sim (n)não")).lower()
        if continuar_pedido == "s":
            continue
        else:
            break


#abaixo caso cliente escreva uma valor acima de 16 ou abaixo de 1 :

    if resposta_cliente > 16:
        print("Digite um número correspondente ao cardapio: de 1 a 16")
        

    if resposta_cliente < 1:
        print("Digite um número correspondente ao cardapio: de 1 a 16")
        
    else:
        ()
print(f"{nome} seu pedido total foi : {carrinho}\n")



# abaixo finalização nao consegui fazer sozinho :
confirmacao_pedido = input("Confirma seu pedido? (s) sim (n) não: ").lower()

while confirmacao_pedido not in ["s", "n"]:
    print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
    confirmacao_pedido = input("Confirma seu pedido? (s) sim (n) não: ").lower()

if confirmacao_pedido == "s":
    print(f"{nome}, Agradecemos seu pedido, em breve sairá para entrega! Tenha uma ótima noite")
elif confirmacao_pedido == "n":
    # Caso escolha Não, mostrar carrinho atual e pedir para remover um item
    while len(carrinho) > 1:  # Continuar enquanto houver mais de um item no carrinho
        print("Carrinho atual:")
        for i, item in enumerate(carrinho, 1):
            print(f"{i}. {item}")

        remover = int(input("Digite o número correspondente ao item que deseja remover: "))
        if remover > 0 and remover <= len(carrinho):
            # Removendo o item do carrinho
            carrinho.pop(remover - 1)
            print("Item removido com sucesso!")
        else:
            print("Número inválido. Tente novamente.")

        confirmacao_novo_pedido = input("Deseja remover mais algum item? (s) sim (n) não: ").lower()
        if confirmacao_novo_pedido == "n":
            break  # Sai do loop se o cliente não quiser mais remover itens
    else:
        print("Só resta um item no carrinho.")

    # Após a finalização da remoção de itens, perguntar se deseja confirmar o pedido
    confirmacao_final = input("Deseja confirmar o pedido? (s) sim (n) não: ").lower()
    if confirmacao_final == "s":
        print(f"{nome} seu pedido total foi : {carrinho}\n")
        print(f"{nome} Agradecemos seu pedido, em breve sairá para entrega para o {endereco}. Tenha uma ótima noite")
    elif confirmacao_final == "n":
        print("Pedido não confirmado.")
    else:
        print("Opção inválida.")
else:
    print("Opção inválida.")
