# Evitando uso de condicionais + Guard Clause

A Guard Clause é uma técnica de programação que consiste em utilizar declarações condicionais no início de uma função para lidar com casos especiais ou condições que precisam ser tratadas de forma diferenciada. Essas declarações condicionais funcionam como uma espécie de "guarda" para evitar a execução desnecessária do restante do código da função quando a condição não é atendida.

Vou fornecer um exemplo de função sem o uso de Guard Clause e outro com o uso dessa técnica em Python para ilustrar a diferença.

Exemplo sem o uso de Guard Clause:

```python
def calcular_divisao(dividendo, divisor):
    if divisor != 0:
        resultado = dividendo / divisor
        return resultado
    else:
        return "Erro: divisão por zero"

print(calcular_divisao(10, 5))  # Saída: 2.0
print(calcular_divisao(10, 0))  # Saída: Erro: divisão por zero
```

Neste exemplo, temos uma função `calcular_divisao` que recebe dois números, `dividendo` e `divisor`. Dentro da função, temos uma declaração condicional que verifica se o `divisor` é diferente de zero. Se essa condição for verdadeira, a divisão é realizada e o resultado é retornado. Caso contrário, uma mensagem de erro é retornada.

Exemplo com o uso de Guard Clause:

```python
def calcular_divisao(dividendo, divisor):
    if divisor == 0:
        return "Erro: divisão por zero"

    resultado = dividendo / divisor
    return resultado

print(calcular_divisao(10, 5))  # Output: 2.0
print(calcular_divisao(10, 0))  # Output: Erro: divisão por zero
```

Neste exemplo, utilizamos a Guard Clause para verificar se o `divisor` é igual a zero. Se essa condição for verdadeira, a função retorna imediatamente a mensagem de erro. Caso contrário, o restante do código é executado para realizar a divisão e retornar o resultado.

A principal diferença entre os dois exemplos é que no primeiro caso o código continua executando até o final da função mesmo quando a condição não é atendida, enquanto no segundo caso a Guard Clause interrompe a execução e retorna imediatamente quando a condição não é atendida. Isso pode ser útil para evitar a execução desnecessária de código ou para tratar casos especiais de forma mais clara e direta.

O uso de Guard Clause pode tornar o código mais legível, evitando a aninhamento excessivo de condicionais ou o uso de blocos de código desnecessários. Ele também pode ajudar a lidar com situações de erro de forma mais explícita e direta.

Lembre-se de que o uso de Guard Clause é uma questão de preferência e estilo de programação. Em alguns casos, pode ser mais adequado utilizar a estrutura condicional tradicional, especialmente quando há a necessidade de executar mais de uma ação ou quando a lógica é mais complexa. A escolha entre os dois métodos depende do contexto e da clareza do código.
