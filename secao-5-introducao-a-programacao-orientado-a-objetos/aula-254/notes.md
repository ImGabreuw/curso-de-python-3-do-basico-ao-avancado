# Teoria: enum.Enum (Enumerações)

Na programação, enumerações são usadas em ocasiões no qual temos um número determinado de valores constantes e com isso queremos agrupar em um tipo.

As enumerações em Python são definidas ao extender da classe `enum.Enum` e essa classe do Python é diferentes das outras uma vez que a metaclasse `EnumType` possui comportamentos únicos.

No Python, enums são um conjunto de nomes simbólicos (membros) ligados a valores únicos e podem ser iterados para retornar seus membros canônicos na ordem de definição.

Para obter os dados de um _Enum_:

- Membro: `membro = Classe(valor)` ou `membro = Classe["chave"]`

- Chave: `Classe.chave.name`

- Valor: `Classe.chave.value`