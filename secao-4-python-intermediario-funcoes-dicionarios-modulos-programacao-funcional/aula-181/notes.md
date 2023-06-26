# O que são ambientes virtuais? (venv)

O `venv` (Virtual Environment) é um módulo integrado ao Python que permite criar ambientes virtuais isolados para projetos Python. Um ambiente virtual é um diretório que contém uma cópia do interpretador Python, bem como uma cópia isolada das bibliotecas e pacotes Python instalados. Essa ferramenta é muito útil para gerenciar dependências e evitar conflitos entre projetos.

Aqui está um exemplo de como usar o `venv` para criar e ativar um ambiente virtual:

1. Crie um ambiente virtual:

   ```
   python -m venv myenv
   ```

Isso criará um novo diretório chamado `myenv`, que conterá o ambiente virtual.

2. Ative o ambiente virtual:

   - No Windows:
     ```
     myenv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source myenv/bin/activate
     ```

Após ativar o ambiente virtual, você verá o nome do ambiente virtual no prompt de comando, indicando que você está dentro do ambiente virtual.

3. Instale pacotes dentro do ambiente virtual:
   Você pode usar o `pip` para instalar pacotes Python no ambiente virtual, e eles serão instalados apenas nesse ambiente isolado. Por exemplo:

   ```
   pip install numpy
   ```

4. Desativar o ambiente virtual:
   Quando você terminar de trabalhar no ambiente virtual, você pode desativá-lo executando o comando `deactivate`:

   ```
   deactivate
   ```

Ao desativar o ambiente virtual, você retornará ao ambiente Python global do sistema.

Ao criar um ambiente virtual usando o `venv`, você pode ter diferentes versões do Python e diferentes conjuntos de pacotes instalados para cada projeto, o que ajuda a evitar conflitos e problemas de dependência entre projetos.

O uso de ambientes virtuais com o `venv` é uma prática recomendada no desenvolvimento Python, pois ajuda a manter um ambiente de trabalho limpo e organizado.
