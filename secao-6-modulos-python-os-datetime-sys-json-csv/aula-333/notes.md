# openpyxl para arquivos Excel xlsx, xlsm, xltx e xltm (instalação)

O OpenPyXL é uma biblioteca Python de código aberto que permite trabalhar com arquivos do Excel nos formatos XLSX, XLSM, XLTX e XLTM. Ele fornece recursos para criar, modificar e manipular planilhas do Excel usando o Python.

Primeiramente, é necessário instalar a biblioteca com o gerenciador de dependências `pip`:

```console
$ pip install openpyxl
```

Aqui está uma breve explicação de cada um desses formatos de arquivo:

1. XLSX (Excel Workbook): É o formato de arquivo padrão para planilhas do Excel a partir da versão 2007. O arquivo XLSX contém várias planilhas, fórmulas, gráficos e formatação, além de suportar recursos avançados do Excel, como macros (VBA). O OpenPyXL pode criar, ler e modificar arquivos XLSX.

2. XLSM (Excel Macro-Enabled Workbook): É semelhante ao formato XLSX, mas permite a inclusão de macros (VBA) no arquivo. Isso significa que você pode executar código VBA dentro do Excel. O OpenPyXL suporta leitura e gravação de arquivos XLSM, mas não executa as macros contidas neles.

3. XLTX (Excel Template): É um formato de arquivo usado para criar modelos ou modelos de planilhas. Ele contém a formatação, as fórmulas e os estilos padrão que serão aplicados a novas planilhas criadas com base no modelo. O OpenPyXL pode ler arquivos XLTX para acessar as configurações de modelo.

4. XLTM (Excel Macro-Enabled Template): É uma versão do formato XLTX que permite a inclusão de macros (VBA). Assim como o XLSM, o OpenPyXL pode ler arquivos XLTM, mas não executa as macros.

Aqui está um exemplo simples de como usar o OpenPyXL para criar um novo arquivo XLSX, adicionar uma planilha e escrever alguns dados nela:

```python
from openpyxl import Workbook

# Cria um novo arquivo XLSX
workbook = Workbook()

# Obtém a planilha ativa (por padrão, sempre é criada uma planilha vazia)
sheet = workbook.active

# Escreve alguns dados na planilha
sheet["A1"] = "Nome"
sheet["B1"] = "Idade"
sheet["A2"] = "João"
sheet["B2"] = 30
sheet["A3"] = "Maria"
sheet["B3"] = 25

# Salva o arquivo
workbook.save("exemplo.xlsx")
```

Esse código cria um novo arquivo XLSX chamado "exemplo.xlsx" e adiciona uma planilha a ele. Em seguida, ele escreve alguns dados nas células A1, B1, A2, B2, A3 e B3 da planilha. Por fim, o arquivo é salvo no disco.
