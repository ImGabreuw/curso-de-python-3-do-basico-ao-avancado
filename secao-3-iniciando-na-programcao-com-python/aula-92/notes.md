# Imprecisão dos números de ponto flutuante + round e decimal.Decimal

> ## **Definição**

O Python e outras linguagens possuem o problema de imprecisão dos números de ponto flutuante, devido a como esse dado é salvo em memória na representação binário. 

> Para mais informações: [double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format).

Como possível solução, o Python fornece uma biblioteca chamada `decimal`:

```python
import decimal

num1 = decimal.Decimal("0.1")
num2 = decimal.Decimal("0.7")

print(num1 + num2) # 0.8
```

> **IMPORTANTE**: sempre colocar o número entre aspas simples ou duplas

Essa biblioteca é recomendada apenas quando há a necessidade de ter uma alta precisão no cálculo com números com ponto flutuante.


> ## **Exemplo**

```python
print(0.1 + 0.7) 
# 0.7999999999999999
```