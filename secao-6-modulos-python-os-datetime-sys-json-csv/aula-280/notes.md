# locale para internacionalização (tradução)

O módulo `locale` do Python fornece funcionalidades para internacionalização (i18n) e localização (l10n) de aplicativos. Ele permite adaptar a formatação de números, datas, moedas e outros elementos de acordo com as convenções culturais e linguísticas de um determinado local.

1. Configuração do ambiente:
   Para usar o módulo `locale`, é necessário configurar o ambiente local adequado para o seu programa. Isso geralmente é feito usando a função `locale.setlocale(category, locale)`.

   Exemplo:

   ```python
   import locale

   # Configura o ambiente local para o idioma e região padrão do sistema
   locale.setlocale(locale.LC_ALL, '')
   ```

2. Formatação de números:
   O módulo `locale` permite formatar números de acordo com as convenções culturais, incluindo a formatação de separadores de milhares e símbolos decimais.

   Exemplo:

   ```python
   import locale

   # Configura o ambiente local para o idioma e região padrão do sistema
   locale.setlocale(locale.LC_ALL, '')

   number = 1234567.89

   # Formata o número de acordo com o ambiente local
   formatted_number = locale.format_string("%f", number)

   print(formatted_number)
   ```

   O resultado do exemplo pode variar dependendo do ambiente local configurado, mas geralmente será algo como "1,234,567.890000".

3. Formatação de moedas:
   O módulo `locale` também permite formatar valores monetários de acordo com as convenções culturais, incluindo o símbolo da moeda, separadores de milhares e símbolos decimais.

   Exemplo:

   ```python
   import locale

   # Configura o ambiente local para o idioma e região padrão do sistema
   locale.setlocale(locale.LC_ALL, '')

   amount = 1234.56

   # Formata o valor monetário de acordo com o ambiente local
   formatted_amount = locale.currency(amount)

   print(formatted_amount)
   ```

   O resultado do exemplo pode variar dependendo do ambiente local configurado, mas geralmente será algo como "$1,234.56" para o idioma inglês.

4. Formatação de datas e horas:
   O módulo `locale` também permite formatar datas e horas de acordo com as convenções culturais, incluindo a ordem dos componentes da data, separadores e nomes dos meses e dias da semana.

   Exemplo:

   ```python
   import locale
   import datetime

   # Configura o ambiente local para o idioma e região padrão do sistema
   locale.setlocale(locale.LC_ALL, '')

   # Obtém a data e hora atual
   now = datetime.datetime.now()

   # Formata a data e hora de acordo com o ambiente local
   formatted_datetime = now.strftime("%c")

   print(formatted_datetime)
   ```

   O resultado do exemplo pode variar dependendo do ambiente local configurado, mas geralmente será algo como "Thu Jul 8 14:37:52 2023" para o idioma inglês.

O módulo `locale` oferece uma ampla gama de recursos para a internacionalização e localização de aplicativos Python. Ele permite adaptar a formatação de números, moedas, datas e horas de acordo com as convenções culturais e linguísticas de um determinado local, tornando seu código mais flexível e adaptável a diferentes regiões e idiomas.

Para mudar o locale para outro idioma no Python, você pode utilizar o módulo `locale` juntamente com a função `setlocale()` para definir o ambiente local desejado. Aqui está um exemplo de como fazer isso:

```python
import locale

# Define o locale para francês (França)
locale.setlocale(locale.LC_ALL, 'fr_FR')

# Exemplo de formatação de números
number = 1234.56
formatted_number = locale.format_string("%f", number)
print(formatted_number)  # Resultado: "1234,560000"

# Exemplo de formatação de moeda
amount = 1234.56
formatted_amount = locale.currency(amount)
print(formatted_amount)  # Resultado: "1 234,56 €"

# Exemplo de formatação de data e hora
import datetime
now = datetime.datetime.now()
formatted_datetime = now.strftime("%c")
print(formatted_datetime)  # Resultado: "jeu. juil.  8 14:37:52 2023"
```

Neste exemplo, o locale foi definido para francês (França) usando o código `'fr_FR'`. Após definir o locale, todas as formatações de números, moedas, datas e horas serão afetadas pelas convenções culturais do novo locale.

Quanto a listar os locales disponíveis no sistema operacional, você pode usar a função `locale.locale_alias.items()` para obter um dicionário contendo todos os locales mapeados no sistema. Cada chave do dicionário representa um nome de locale e o valor é o código correspondente. Aqui está um exemplo de como listar os locales disponíveis:

```python
import locale

# Obtém os locais disponíveis no sistema
locales = locale.locale_alias.items()

# Imprime os locais
for name, value in locales:
    print(name, "=>", value)
```

A saída desse exemplo será uma lista de todos os nomes de locale seguidos pelos códigos correspondentes, como por exemplo:

```
afrikaans_za => af_ZA
afrikaans_za.iso88591 => af_ZA.ISO8859-1
afrikaans_za.utf8 => af_ZA.UTF-8
amharic_et => am_ET
amharic_et.utf8 => am_ET.UTF-8
...
```

Essa lista pode ser útil para verificar os locales disponíveis no sistema operacional e escolher qual usar ao definir o ambiente local em seu código Python.

Outra maneira de obter os locales disponíveis no seu sistema operacional é utilizar comandos no terminal:

No Windows:

```console
$ Get-WinSystemLocale
```

No Linux/MacOS:

```console
$ locale -a
```
