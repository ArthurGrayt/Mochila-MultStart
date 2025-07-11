# Mochila MultStart

# Função da mochila 

def mochila(valores, pesos_itens, capacidade, ordem_itens):
    valor_total = 0  # valor total acumulado da mochila com 0
    peso_total = 0   # peso total acumulado da mochila com 0
    itens_mochila = []  # lista para guardar os itens que foram escolhidos
    for i in ordem_itens:
        if peso_total + pesos_itens[i] <= capacidade:
            peso_total += pesos_itens[i]  # Add o peso do item ao peso total
            valor_total += valores[i]   # Add o valor do item ao valor total
            itens_mochila.append(i)  # add no fim da lista itens_mochila
    return valor_total, peso_total, itens_mochila  # retornando resultados

