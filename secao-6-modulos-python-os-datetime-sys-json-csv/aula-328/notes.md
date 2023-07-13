# PyPDF2 para manipular arquivos PDF (PdfReader)

_PdfReader_ é uma classe dentro do módulo _PyPDF_ para manipular PDFs. Para fazer isso, é necessário especificar o caminho do arquivo ao instanciar essa classe.

```python
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
```

Para você obter as páginas de um PDF, basta utilizar `reader.pages` o qual retorna uma lista contendo cada página:

```python
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")

print(len(reader.pages))

for page in reader.pages:
    print(page)
```

Você pode extrair texto e imagens de uma página específica:

```python
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")

page0 = reader.pages[0]

print(page0.extract_text())
print(page0.images)
```

Além disso, você pode salvar uma imagem específica do PDF na sua máquina:

```python
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")

page0 = reader.pages[0]
imagem0 = page0.images[0]

print(page0.extract_text())
with open(imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)
```