# Formatando datas do datetime com strftime no Python

Para formatar datas em Python com o módulo `datetime`, existe o método `strftime( [formato] )`. Veja o exemplo abaixo:

```python
from datetime import datetime

hoje = datetime.now()

print(hoje.strftime("%d/%m/%Y")) # Saída: 08/07/2023
print(hoje.strftime("%d/%m/%Y %H:%M")) # Saída: 08/07/2023 18:01
print(hoje.strftime("%d/%m/%Y %H:%M:%S")) # Saída: 08/07/2023 18:01:38
```