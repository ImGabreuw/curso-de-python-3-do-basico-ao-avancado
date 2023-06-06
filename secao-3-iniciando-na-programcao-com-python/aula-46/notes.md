# Fatiamento de strings e a função len

> ## **Definição**

A indexação dos caracteres de uma string é feita da seguinte forma:

```python
 012345678
"Olá mundo"
-987654321 
```

Dessa forma, o fatiamento da string é feito por meio de um início (inclusivo), fim (exclusivo) e o passo:

```python
"string"[[início]:[fim]:[passo]]
```

Os argumentos `[início]`, `[fim]` e `[passo]` são opcionais. Sendo assim, em caso de não for especificado um valor para esses argumentos, o Python assumirá os valores padrão:

- `[início]`: `0`

- `[fim]`= tamanho da string

- `[passo]` = `1` (irá percorrer o intervalo de 1 em 1)

É possível utilizar valores negativos.

```python
print("Olá mundo!"[::-1]) # !odnum álO
```

> `[passo]` como `-1`, irá inverter a string

> ## **Exemplo**

```python
print("Olá mundo"[4:8:2]) # mm
print("Olá mundo"[4:8]) # mund
print("Olá mundo"[4:]) # mundo
```