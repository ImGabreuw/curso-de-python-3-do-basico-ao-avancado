# string.Template para substituir variáveis em textos

A classe `string.Template` é uma maneira conveniente de substituir variáveis em textos predefinidos. Ela permite definir um modelo de texto com espaços reservados para variáveis e, em seguida, substituir esses espaços reservados pelos valores desejados.

Para usar `string.Template` junto com a função `open` para substituir variáveis em textos, você pode seguir os seguintes passos:

Passo 1: Crie um arquivo de modelo de texto

Primeiro, crie um arquivo de texto que servirá como modelo, contendo espaços reservados para as variáveis que você deseja substituir. Você pode usar a sintaxe `${variavel}` ou `$variavel` para definir os espaços reservados.

Exemplo de arquivo de modelo chamado `template.txt`:

```
Olá, ${nome}!

Seu número de cliente é ${numero_cliente}.
Seu saldo atual é $${saldo}.
```

Passo 2: Abra o arquivo e substitua as variáveis

Em seguida, você pode abrir o arquivo usando a função `open` e ler seu conteúdo. Depois, você pode criar uma instância de `string.Template` usando o conteúdo do arquivo como modelo.

Exemplo:

```python
from string import Template

with open('template.txt', 'r') as file:
    template_content = file.read()

template = Template(template_content)
```

Passo 3: Substitua as variáveis

Agora você pode usar os métodos `substitute` ou `safe_substitute` para substituir as variáveis pelo seu valor desejado. A diferença entre esses métodos é que `substitute` levanta uma exceção KeyError se alguma variável não for fornecida, enquanto `safe_substitute` simplesmente mantém o espaço reservado se uma variável não for encontrada.

Exemplo usando `substitute`:

```python
substituicoes = {
    'nome': 'João',
    'numero_cliente': '123456',
    'saldo': '100.00'
}

texto_substituido = template.substitute(substituicoes)
print(texto_substituido)
```

Saída:

```
Olá, João!

Seu número de cliente é 123456.
Seu saldo atual é $100.00.
```

Exemplo usando `safe_substitute`:

```python
substituicoes = {
    'nome': 'Maria',
    'saldo': '50.00'
}

texto_substituido = template.safe_substitute(substituicoes)
print(texto_substituido)
```

Saída:

```
Olá, Maria!

Seu número de cliente é ${numero_cliente}.
Seu saldo atual é $50.00.
```

Observe que no segundo exemplo, a variável `numero_cliente` não foi fornecida, mas `safe_substitute` não levanta uma exceção e mantém o espaço reservado no texto resultante. Isso pode ser útil em situações em que nem todas as variáveis precisam ser substituídas obrigatoriamente.

Além disso, é possível criar um template personalizado herdando da classe `string.Template`. A classe `string.Template` fornece um mecanismo flexível para a criação de templates de strings, permitindo substituir partes específicas do texto por valores dinâmicos. Ao criar um template herdando da classe `string.Template`, você pode adicionar funcionalidades extras ou personalizar o comportamento do template de acordo com suas necessidades.

Aqui está um exemplo de como criar um template personalizado herdando da classe `string.Template`:

```python
from string import Template

class MeuTemplate(Template):
    delimiter = '%'  # Define o delimitador para substituições no template

# Exemplo de uso do template personalizado
template = MeuTemplate('Olá, %{nome}! Seu saldo é %{saldo}.')

# Preenche o template com os valores fornecidos
mensagem = template.substitute(nome='João', saldo='R$ 100,00')

print(mensagem)
```

Neste exemplo, a classe `MeuTemplate` herda da classe `Template` e define o delimitador para substituições no template como `%`.

```console
Olá, João! Seu saldo é R$ 100,00.
```

Em seguida, criamos uma instância do template personalizado, fornecendo o texto do template no construtor. Podemos então chamar o método `substitute` no template para preencher as substituições com os valores desejados. No exemplo, substituímos `%{nome}` por `'João'` e `%{saldo}` por `'R$ 100,00'`.
