# PyPDF2 para manipular arquivos PDF (PdfMerger)

_PdfMerger_ é uma classe do módulo _PyPDF2_ para unir PDFs em um único. Veja o exemplo abaixo:

```python
files = ['page0.pdf', 'page1.pdf']
merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write('MERGED.pdf')
merger.close()
```
