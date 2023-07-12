# (Parte 1) ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile

A biblioteca `zipfile` em Python permite compactar e descompactar arquivos no formato ZIP. Ela fornece classes e métodos para criar, abrir, ler, escrever e extrair arquivos ZIP. Aqui está um exemplo de como usar a biblioteca `zipfile` para compactar e descompactar arquivos.

```python
import zipfile

# Compactando arquivos em um arquivo ZIP
def compactar_arquivos(nome_zip, arquivos):
    with zipfile.ZipFile(nome_zip, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo)

# Descompactando arquivos de um arquivo ZIP
def descompactar_arquivos(nome_zip, pasta_destino):
    with zipfile.ZipFile(nome_zip, 'r') as zipf:
        zipf.extractall(pasta_destino)

# Exemplo de uso

# Compactando arquivos
arquivos_para_compactar = ['arquivo1.txt', 'arquivo2.txt', 'pasta/arquivo3.txt']
compactar_arquivos('arquivos.zip', arquivos_para_compactar)

# Descompactando arquivos
pasta_destino = 'pasta_destino'
descompactar_arquivos('arquivos.zip', pasta_destino)
```

No exemplo acima, a função `compactar_arquivos` recebe o nome do arquivo ZIP que será criado e uma lista de caminhos de arquivos que serão compactados. Em seguida, ele itera sobre a lista de arquivos e adiciona cada um deles ao arquivo ZIP usando o método `write()`.

A função `descompactar_arquivos` recebe o nome do arquivo ZIP a ser descompactado e o caminho para a pasta onde os arquivos serão extraídos. Ela usa o método `extractall()` para extrair todos os arquivos contidos no arquivo ZIP para a pasta de destino especificada.

É importante observar que a biblioteca `zipfile` suporta vários outros recursos, como adicionar senhas aos arquivos compactados, adicionar comentários, modificar arquivos existentes em um arquivo ZIP e muito mais. Você pode consultar a documentação oficial do Python para obter mais informações sobre a biblioteca `zipfile`: https://docs.python.org/3/library/zipfile.html
