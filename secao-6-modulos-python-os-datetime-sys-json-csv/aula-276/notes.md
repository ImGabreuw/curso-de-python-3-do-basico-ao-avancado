# datetime.timedelta e dateutil.relativedelta (calculando datas)

Para calcular a diferença entre duas datas, basta utilizar o operador de subtração (`-`).

```python
from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = data_fim - data_inicio
print(delta.days, delta.seconds, delta.microseconds)

# Saída: 13019 82190 0
```

Como pode-se observar a diferença é feita entre unidades iguais de uma data, ou seja, `delta.days` é refente a diferença em dias entre `data_inicio` e `data_fim`.

Agora caso você queira a diferença total entre 2 datas, basta usar a o método `total_seconds()` que retorna essa diferença em segundos.

```python
from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = data_fim - data_inicio
print(delta.total_seconds())

# Saída: 1124923790.0
```

Além disso é possível verificar se uma data é igual, posterior ou anterior a uma data de referência. Veja o exemplo abaixo:

```python
from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = data_fim - data_inicio
print(data_fim > data_inicio) # Saída: True
print(data_fim < data_inicio) # Saída: False
print(data_fim == data_inicio) # Saída: False
```

Caso você queira criar uma data com um espaçamento temporal específico em relação a uma data de referência, basta utilizar a classe `timedelta`.

Supondo que você queira criar uma nova data com uma diferença de 10 dias no futuro do dia atual, então teremos:

```python
from datetime import datetime, timedelta

hoje = datetime.now()
delta = timedelta(days=10)

print(hoje + delta) # Saída: 2023-07-18 17:42:57.384756
```

### **Módulo `python-dateutil`**

Antes de tudo temos que instalar o módulo na máquina local ou no ambiente virtual Python:

```console
$ pip install python-dateutil types-python-dateutil
```

> **OBS**: o módulo `types-python-dateutil` são as tipagens de `python-dateutil` e são necessárias apenas para desenvolvedores que usam alguma linter de código.

Como ele é possível fazer exatamente as mesmas coisas com a classe `timedelta` do Python, porém com muitas facilidades.

Podemos adicionar segundos, minutos, etc na data de referência:

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

hoje = datetime.now()

print(hoje) # Saída: 2023-07-08 17:51:32.422844
print(hoje + relativedelta(seconds=60, minutes=10)) # Saída: 2023-07-08 18:02:32.422844
```

Além disso, podemos pegar a diferençar entre duas datas.

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

print(relativedelta(data_fim, data_inicio))

# Saída: relativedelta(years=+35, months=+7, days=+21, hours=+22, minutes=+49, seconds=+50)
```
