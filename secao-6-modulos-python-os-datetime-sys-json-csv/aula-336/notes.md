# openpyxl - ler e alterar dados de uma planilha

O OpenPyXL permite ler e alterar dados de uma planilha do Excel de forma fácil e flexível. Você pode acessar as células, obter seus valores, modificar os valores existentes e adicionar novos dados conforme necessário. Aqui está uma explicação geral de como ler e alterar dados em uma planilha usando o OpenPyXL, seguida de um exemplo prático.

1. Acessando células: Você pode acessar células específicas usando a notação de índice ou o método `sheet.cell(row, column)`, onde `row` é o número da linha e `column` é o número da coluna. Por exemplo, `sheet['A1']` ou `sheet.cell(row=1, column=1)`.

2. Lendo o valor das células: Para ler o valor de uma célula, você pode acessar a propriedade `cell.value`. Por exemplo, `valor = sheet['A1'].value`.

3. Modificando o valor das células: Para alterar o valor de uma célula existente, você pode atribuir um novo valor à propriedade `cell.value`. Por exemplo, `sheet['A1'].value = 'Novo Valor'`.

4. Iterando sobre as células: Você pode iterar sobre as células de uma coluna ou linha específica usando o método `sheet.iter_rows()` ou `sheet.iter_cols()`. Isso permite percorrer e acessar os valores de várias células de uma vez.

5. Adicionando dados: Para adicionar novos dados à planilha, você pode simplesmente acessar uma célula vazia e atribuir um valor a ela. Você também pode usar métodos como `sheet.append()` para adicionar várias linhas de dados de uma só vez.

Aqui está um exemplo prático que demonstra como ler e alterar dados em uma planilha usando o OpenPyXL:

```python
from openpyxl import load_workbook

# Carrega o arquivo existente
workbook = load_workbook('exemplo.xlsx')

# Acessa a planilha desejada
sheet = workbook['Planilha1']

# Lê o valor de uma célula
valor = sheet['A1'].value
print(f"Valor atual em A1: {valor}")

# Modifica o valor de uma célula
sheet['A1'].value = 'Novo Valor'

# Itera sobre as células em uma coluna
for row in sheet.iter_rows(min_row=2, max_row=5, min_col=1, max_col=1):
    for cell in row:
        print(cell.value)

# Adiciona novos dados à planilha
sheet.append(['Nome', 'Idade'])
sheet.append(['Maria', 25])
sheet.append(['João', 30])

# Salva as alterações no arquivo
workbook.save('exemplo.xlsx')
```

Nesse exemplo, o código carrega um arquivo existente chamado 'exemplo.xlsx' e acessa a planilha 'Planilha1'. Ele lê o valor da célula A1, modifica o valor da célula A1 para 'Novo Valor' e itera sobre as células da coluna A nas linhas 2 a 5. Em seguida, o código adiciona novos dados à planilha usando o método `sheet.append()`. Por fim, as alterações são salvas no arquivo.