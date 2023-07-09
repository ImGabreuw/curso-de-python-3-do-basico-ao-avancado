# json.dumps e json.loads com strings + typing.TypedDict

O método `json.dumps()` é usado para converter um objeto Python em uma string JSON (serialização), enquanto o método `json.loads()` é usado para converter uma string JSON em um objeto Python (desserialização).

> **OBS**: o `s` nos métodos `dumps()` e `loads()` é uma abreviação de string.

Quando se trabalha com strings JSON, é possível utilizar a biblioteca `typing` do Python para definir tipos mais precisos para os dados, como `TypedDict`, que permite definir uma estrutura de dicionário com tipos específicos para as chaves e valores.

Aqui está um exemplo que utiliza `json.dumps()` e `json.loads()` com strings JSON e `TypedDict`:

```python
import json
from typing import TypedDict

# Definindo um TypedDict para representar informações de uma pessoa
class Pessoa(TypedDict):
    nome: str
    idade: int
    casado: bool

# Criando um objeto Pessoa
pessoa = Pessoa(nome="João", idade=30, casado=True)

# Convertendo objeto Pessoa em string JSON
json_string = json.dumps(pessoa)
print(json_string)
# Saída: {"nome": "João", "idade": 30, "casado": true}

# Convertendo string JSON em objeto Pessoa
pessoa_de_json = json.loads(json_string, object_hook=Pessoa)
print(pessoa_de_json)
# Saída: {'nome': 'João', 'idade': 30, 'casado': True}
```

Nesse exemplo, `Pessoa` é um `TypedDict` que representa as informações de uma pessoa, com chaves `nome`, `idade` e `casado`, e seus respectivos tipos (`str`, `int` e `bool`).

O objeto `pessoa` é criado como um `Pessoa`, com valores específicos para cada campo. Em seguida, o `json.dumps()` é usado para serializar o objeto em uma string JSON (`json_string`), que é impressa na saída.

Após isso, `json.loads()` é utilizado para deserializar a string JSON (`json_string`) de volta em um objeto Python. O argumento `object_hook=Pessoa` é usado para indicar que o objeto resultante deve ser mapeado para o tipo `Pessoa`. O resultado é atribuído à variável `pessoa_de_json`, que é impressa na saída.

Outra forma de você mapear o JSON para o tipo `Pessoa` é simplesmente definir o tipo explicitamente da variável que o armazena:

```python
pessoa_de_json: Pessoa = json.loads(json_string)
print(pessoa_de_json)
# Saída: {'nome': 'João', 'idade': 30, 'casado': True}
```

Além disso, o método `json.dumps()` também permite formatar a saída JSON para torná-la mais legível e organizada. A formatação é especialmente útil ao lidar com objetos JSON complexos. Podemos utilizar o parâmetro `indent` para especificar o nível de recuo desejado na formatação e o parâmetro `ensure_ascii` para forçar a conversão de caracteres especiais em códigos ASCII.

Aqui está um exemplo que demonstra a formatação de um objeto Python em uma string JSON formatada usando `json.dumps()`:

```python
import json

dados = {
    "nome": "João",
    "idade": 30,
    "casado": True,
    "filhos": ["Maria", "Pedro"],
    "endereco": {
        "rua": "Rua Principal",
        "cidade": "São Paulo",
        "estado": "SP"
    }
}

json_string = json.dumps(dados, ensure_ascii=False, indent=4)
print(json_string)
```

Nesse exemplo, o objeto `dados` representa informações sobre uma pessoa, incluindo nome, idade, estado civil, filhos e endereço. Ao usar `json.dumps()` com o parâmetro `indent=4`, a string JSON será formatada com um recuo de 4 espaços, tornando-a mais legível e organizada. A saída seria:

```
{
    "nome": "João",
    "idade": 30,
    "casado": true,
    "filhos": [
        "Maria",
        "Pedro"
    ],
    "endereco": {
        "rua": "Rua Principal",
        "cidade": "São Paulo",
        "estado": "SP"
    }
}
```

Observe que cada nível do objeto JSON é recuado por 4 espaços, facilitando a visualização da estrutura do JSON. A formatação pode ser ajustada alterando o valor do parâmetro `indent` para o número desejado de espaços de recuo.

Essa formatação é útil para visualização, depuração e leitura de objetos JSON, especialmente quando trabalhamos com estruturas mais complexas.

Assim, com `json.dumps()` e `json.loads()` é possível converter objetos Python em strings JSON e vice-versa, enquanto `TypedDict` permite definir a estrutura dos dados com tipos específicos para uma manipulação mais segura e consistente.
