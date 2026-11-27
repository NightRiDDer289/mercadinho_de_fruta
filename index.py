# ==========================================
#   MERCADINHO DE FRUTAS
# ==========================================

# ------------------------------------------
# 1. VARIÁVEIS E TIPOS

nome_loja = "Mercadinho de fruta"
ano_abertura =  2020
loja_aberta = True
taxa_entrega = 5.2


print(f"boas vindas a loja {nome_loja}, aberta des de {ano_abertura}, e nossa taxa de entrega é de {taxa_entrega}")

print(type(nome_loja))
print(type(ano_abertura))
print(type(loja_aberta))
print(type(taxa_entrega))

# 2 - carrinho de fruta (gabriel)

carrinho = ["maça","uva","pera","banana"]

# 3. Criar o array de preços e o array de estoque e criar uma função de exibir as frutas (vitor)

preco = [5.00, 15.00, 7.00, 10.00]
estoque = [5, 2, 5, 3]

def mostrar_frutas():
    for i in range(len(carrinho)):
        print(carrinho[i])

mostrar_frutas()