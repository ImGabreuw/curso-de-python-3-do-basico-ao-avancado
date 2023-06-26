# Criando e usando um requirements.txt

O arquivo `requirements.txt` é um arquivo de texto utilizado no Python para especificar as dependências de um projeto. Ele contém uma lista dos pacotes e suas versões correspondentes que são necessários para o projeto funcionar corretamente.

O `requirements.txt` é comumente usado em conjunto com o `pip` para instalar todas as dependências de um projeto de uma só vez. Isso facilita a replicação do ambiente de desenvolvimento em diferentes máquinas e garante que todas as bibliotecas necessárias sejam instaladas corretamente.

Aqui está um exemplo de como criar e usar o `requirements.txt`:

1. Crie o arquivo `requirements.txt`:
   Abra um editor de texto e crie um novo arquivo chamado `requirements.txt`. Cada linha desse arquivo deve conter o nome do pacote e, opcionalmente, a versão especificada. Por exemplo:

   ```
   requests==2.26.0
   numpy==1.21.0
   matplotlib
   ```

   No exemplo acima, estamos especificando a versão 2.26.0 do pacote `requests`, a versão 1.21.0 do pacote `numpy` e a versão mais recente disponível do pacote `matplotlib`.

2. Instale as dependências a partir do `requirements.txt`:
   Com o arquivo `requirements.txt` criado, você pode usar o comando `pip` para instalar todas as dependências listadas nele. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo `requirements.txt` está localizado. Em seguida, execute o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

   O `pip` lerá o arquivo `requirements.txt` e instalará todas as dependências especificadas nele, garantindo que as versões corretas sejam utilizadas.

Esse é um exemplo básico de como usar o `requirements.txt`. É importante manter o arquivo `requirements.txt` atualizado à medida que novas dependências forem adicionadas ao projeto ou quando as versões das dependências mudarem.

Além disso, é possível gerar o arquivo `requirements.txt` automaticamente a partir do ambiente atual usando o comando `pip freeze`. Por exemplo:

```
pip freeze > requirements.txt
```

Isso criará um arquivo `requirements.txt` contendo todas as dependências e suas versões exatas do ambiente atual. Essa abordagem é útil para compartilhar o ambiente de desenvolvimento com outras pessoas ou para garantir uma configuração consistente do ambiente em diferentes máquinas.

O `requirements.txt` é uma ferramenta valiosa para gerenciar as dependências de um projeto Python e garantir a consistência do ambiente de desenvolvimento.
