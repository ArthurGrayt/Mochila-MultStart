# Mochila 0-1 com Multistart

Esse projeto resolve o problema da mochila 0-1 usando Multistart.  
A ideia é testar várias combinações diferentes de itens para tentar encontrar a melhor solução possível, considerando também o limite de peso.

## Como funciona

- Cada item tem um valor e um peso.
- A mochila tem uma capacidade máxima.
- O programa tenta 1000 vezes montar a mochila com diferentes combinações aleatórias.
- A melhor solução entre essas tentativas é mostrada no final.

Antes de começar as tentativas aleatórias, também testei uma solução gulosa, que escolhe os itens pela melhor relação valor/peso. Serve como comparação.

## Como executar

É só ter o Python instalado. Depois, rode:

```bash
python src/mochila_multistart.py
