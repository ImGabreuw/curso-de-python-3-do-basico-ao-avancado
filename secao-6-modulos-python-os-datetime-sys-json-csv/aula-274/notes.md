# Criando data e hora em Python com módulo datetime

O módulo `datetime` em Python fornece classes e funções para trabalhar com datas e horas.

### `strptime`

A função `strptime` converte uma string em um objeto `datetime` com base em um formato especificado.

Exemplo:
Vamos supor que temos uma string que representa uma data no formato "dd/mm/aaaa" e queremos convertê-la em um objeto `datetime`:

```python
from datetime import datetime

date_string = '12/07/2023'
date_object = datetime.strptime(date_string, '%d/%m/%Y')
print(date_object)  # Saída: 2023-07-12 00:00:00
```

Nesse exemplo, usamos a função `strptime` para converter a string `date_string` em um objeto `datetime`. O segundo argumento da função é o formato da string de data especificado como uma diretiva de formatação `%d` para o dia, `%m` para o mês e `%Y` para o ano com quatro dígitos.

### `datetime(ano, mes, dia)`

A função `datetime` cria um objeto `datetime` com a data fornecida, sem especificar a hora, minuto e segundo.

Exemplo:
Vamos criar um objeto `datetime` representando a data 1º de janeiro de 2022:

```python
from datetime import datetime

date_object = datetime(2022, 1, 1)
print(date_object)  # Saída: 2022-01-01 00:00:00
```

Nesse exemplo, usamos a função `datetime` para criar um objeto `datetime` representando a data 1º de janeiro de 2022. O objeto resultante terá a hora, minuto e segundo definidos como 0.

### `datetime(ano, mes, dia, hora, minuto, segundo)`

A função `datetime` cria um objeto `datetime` com a data e hora fornecidas.

Exemplo:
Vamos criar um objeto `datetime` representando a data e hora 25 de dezembro de 2022 às 10:30:45:

```python
from datetime import datetime

datetime_object = datetime(2022, 12, 25, 10, 30, 45)
print(datetime_object)  # Saída: 2022-12-25 10:30:45
```

Nesse exemplo, usamos a função `datetime` para criar um objeto `datetime` representando a data e hora específicas. Passamos o ano, mês, dia, hora, minuto e segundo como argumentos para a função.

Observe que todas as funções `datetime` retornam um objeto `datetime` que contém informações sobre a data e hora especificadas. Esses objetos `datetime` oferecem métodos e atributos úteis para manipular e realizar operações com datas e horas, como cálculos de diferença, formatação, comparação e muito mais.
