# PyPDF2 para manipular arquivos PDF (PdfWriter)

_PdfWriter_ é uma classe do módulo _PyPDF2_ para criar PDFs. Veja o exemplo abaixo:

```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("example.pdf")

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
```
