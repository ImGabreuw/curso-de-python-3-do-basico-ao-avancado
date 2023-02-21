# Ubuntu 22 - Instalação básica do Python e o VS Code

> ## **Instalação do Python**

1. Atualização dos repositórios e pacotes do Ubuntu

   ```shell
   $ sudo apt update -y && sudo apt upgrade -y
   ```

2. Instalação de pacotes para desenvolvimento (não relacionados ao Python)

   ```shell
   $ sudo apt install git curl build-essential gcc make default-libmysqlclient-dev libssh-dev
   ```

3. Instalação do Python na versão 3.10

   ```shell
   $ sudo apt install python3.10
   ```

4. Criar um ambiente virtual Python

   ```shell
   $ python3 -m venv [nome do ambiente]
   ```

   > flag `-m`: executar um módulo do Python como se fosse um script

   ```shell
   $ python3 -m venv venv
   ```

5. Ativar o ambiente virtual Python

   ```shell
   $ source venv/bin/activate
   ```

   **OU**

   ```shell
   $ . venv/bin/activate
   ```

6. Testar o ambiente virtual Python

   ```shell
   $ python -V
   # Python 3.11.0
   ```

   ```shell
   $ which python
   # /home/gabriel/Projects/curso-de-python-3-do-basico-ao-avancado/secao-2-python-vscode-preparando-meu-ambiente-de-desenvolvimento/ubuntu-22-instalacao-basica-do-python-e-o-vscode/projetos/venv/bin/python
   ```

7. Instalação de libs no ambiente virtual

   ```shell
   $ python install pymysql
   ```

   > A instalação dessas libs estará em `/venv/lib/python3.11/site-packages`

8. (Opcional) Caso apareça um aviso, no _passo 7_, para atualizar o `pip` executar o seguinte comando:

   ```shell
   $ python -m pip install pip --upgrade
   ```

9. Fechar o ambiente virtual:

   ```shell
   $ deactivate
   ```

> ## **Instalação do VS Code**

1. Acessar a aba `downloads` no site oficial do VS Code:

   https://code.visualstudio.com/download

2. Baixar o executável para o seu sistema operacional

3. Executar o instalador do VS Code:

   ```shell
   $ sudo dpkg -i [executável]
   ```

4. Iniciar o VS Code:

   ```shell
   $ code
   ```

> ## **Primeiros passos no Python**

1. Criar um aquivo com a extensão `.py`

2. Inserir o seguinte código no arquivo

   ```python
   print("Hello World!")
   ```

3. Executar o arquivo:

   ```shell
   $ python [nome do arquivo]
   ```

   ```shell
   $ python main.py
   # Hello World!
   ```
