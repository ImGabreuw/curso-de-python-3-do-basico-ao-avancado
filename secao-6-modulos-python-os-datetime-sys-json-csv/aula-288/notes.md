# O que é JSON - JavaScript Object Notation

JSON (JavaScript Object Notation) é um formato de dados leve e amplamente utilizado para troca de informações estruturadas entre diferentes sistemas. No Python, o módulo `json` é responsável por trabalhar com JSON, fornecendo funções para conversão de tipos de Python para JSON e vice-versa.

Os tipos suportados em JSON incluem:

1. Objeto (Object): É um conjunto não ordenado de pares chave-valor, delimitado por chaves `{}`. As chaves são strings e os valores podem ser de qualquer tipo JSON válido.
2. Array (Array): É uma coleção ordenada de valores, delimitado por colchetes `[]`. Os valores podem ser de qualquer tipo JSON válido.
3. String (String): É uma sequência de caracteres delimitada por aspas duplas `" "`.
4. Número (Number): Pode ser um inteiro, número de ponto flutuante ou notação exponencial.
5. Booleano (Boolean): Pode ser `true` ou `false`.
6. Nulo (Null): Representa um valor nulo ou vazio.

A conversão de tipos em Python para JSON, em geral, seguem a seguinte relação:

|   Python    |  JSON  |
| :---------: | :----: |
|    dict     | object |
| list, tuple | array  |
|     str     | string |
| int, float  | number |
|    True     |  true  |
|    False    | false  |
|    None     |  null  |

Veja um exemplo de dados no formato JSON:

```json
{
  "nome": "João",
  "idade": 30,
  "casado": true,
  "filhos": ["Maria", "Pedro"],
  "endereco": {
    "rua": "Rua Principal",
    "cidade": "São Paulo",
    "estado": "SP"
  }
}
```

**IMPORTANTE**: no final de cada linha é obrigatório colocar vírgula (`,`).
