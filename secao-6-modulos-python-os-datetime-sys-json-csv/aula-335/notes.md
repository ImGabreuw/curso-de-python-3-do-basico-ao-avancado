# openpyxl - manipulando as planilhas do Workbook

O OpenPyXL fornece recursos poderosos para manipular as planilhas de um arquivo Workbook. Aqui está uma explicação geral de como trabalhar com as planilhas usando o OpenPyXL, seguida de um exemplo que demonstra várias operações comuns.

1. Acessando planilhas existentes: Ao abrir um arquivo Workbook com o OpenPyXL, você pode acessar as planilhas existentes usando o método `workbook[sheet_name]`, onde `sheet_name` é o nome da planilha desejada. Você também pode acessar a planilha ativa usando `workbook.active`.

2. Criando novas planilhas: Você pode criar uma nova planilha usando o método `workbook.create_sheet(title)`, onde `title` é o título/nome da nova planilha. Você pode especificar a posição da nova planilha usando o argumento `index`.

3. Removendo planilhas: Para remover uma planilha do Workbook, você pode usar o método `workbook.remove(sheet)`, onde `sheet` é a planilha que você deseja remover.

4. Renomeando planilhas: Para renomear uma planilha, você pode usar a propriedade `sheet.title`, onde `sheet` é a planilha que você deseja renomear.

5. Acessando células e seus valores: Você pode acessar as células de uma planilha usando a notação de índice, como `sheet["A1"]` ou `sheet.cell(row=1, column=1)`. Você pode obter o valor de uma célula usando a propriedade `cell.value`.

6. Escrevendo dados nas células: Você pode escrever dados em uma célula atribuindo um valor à propriedade `cell.value`. Por exemplo, `sheet["A1"] = "Exemplo"` ou `sheet.cell(row=2, column=1, value=42)`.

Aqui está um exemplo que demonstra várias operações comuns de manipulação de planilhas usando o OpenPyXL:

```python
from openpyxl import Workbook, load_workbook

# Carrega um arquivo existente
workbook = load_workbook("exemplo.xlsx")

# Acessa uma planilha existente
sheet = workbook["Sheet1"]

# Renomeia uma planilha
sheet.title = "Planilha1"

# Cria uma nova planilha
nova_planilha = workbook.create_sheet(title="Planilha2", index=1)

# Remove uma planilha
sheet_para_remover = workbook["Sheet2"]
workbook.remove(sheet_para_remover)

# Escreve dados nas células
sheet["A1"] = "Nome"
sheet["B1"] = "Idade"
sheet["A2"] = "João"
sheet["B2"] = 30
sheet["A3"] = "Maria"
sheet["B3"] = 25

# Acessa e atualiza o valor de uma célula
célula = sheet["A1"]
célula.value = "Nome Completo"

# Obtém o valor de uma célula
valor_célula = sheet["B2"].value

# Salva as modificações no arquivo
workbook.save("exemplo.xlsx")
```

Nesse exemplo, o código carrega um arquivo existente chamado "exemplo.xlsx" e realiza várias operações nas planilhas. Ele renomeia a planilha "Sheet1" para "Planilha1", cria uma nova planilha chamada "Planilha2" na segunda posição e remove a planilha "Sheet2". Em seguida, ele escreve dados em várias células, acessa e atualiza o valor de uma célula específica e obtém o valor de outra célula. Por fim, as modificações são salvas no arquivo.
