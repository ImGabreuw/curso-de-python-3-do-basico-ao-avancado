# Formatação de strings com f-strings

> ## **Padding em strings**

É possível adicionar um _padding_ em string para mantê-la com um tamanho fixo.

Há 3 estilos de _padding_:

- À esquerda com `>`

- À direita com `<`

- Ao centro com `^`

Por padrão, o caractere de espaço é utilizado para completar os espaços faltantes de uma string. Entretanto é possível alterá-lo com a seguinte sintaxe:

```python
f"{[valor]:[caractere][><^][tamanho da string]}"
```

```python
var = "ABC"

print(f"{var}")       # "ABC"
print(f"{var: >10}")  # "       ABC"
print(f"{var: <10}")  # "ABC       "
print(f"{var: ^10}")  # "   ABC    "
```

> ## **Formatação de números**

Para formatar um número flutuante com N casas decimais, basta utilizar o seguinte formato:

```python
f"{[número]:.[número de casas]f}"
```

```python
print(f"{3.1415:.2f}") # 3.14
```

Caso queira formatar um número com o separador de milhar:

```python
f"{[número]:,}"

# OU

f"{[número]:,.[número de casas]f}"
```

```python
print(f"{100_000_000:,}") # 100,000,000
print(f"{100_000_000.1567:,.2f}") # 100,000,000.16
```

É possível formatar um número para mostrar explicitamente o sinal dele:

> **OBS**: é padrão é mostrar apenas o sinal de `-`, caso o número seja negativo

```python
f"{[número]:+}"
```

```python
print(f"{10:+}") # +10
```

A conversão um decimal para hexadecimal é similar com a interpolação:

```python
f"{[número decimal]:[dígitos]x}"

# OU

f"{[número decimal]:[dígitos]X}"
```

```python
print(f"1500 em haexadecimal é {1500:08x}") # 1500 em haexadecimal é 000005dc
print(f"1500 em haexadecimal é {1500:08X}") # 1500 em haexadecimal é 000005DC
```

> ## **Conversion flags**

Há 3 _conversion flags_ no f-strings e eles servem para invocar os seguintes métodos:

- `!r`: `__repr__()`

- `!s`: `__str__()`

- `!a`: `ascii()`

```python
f"{[valor]!r}"

f"{[valor]!s}"

f"{[valor]!a}"
```