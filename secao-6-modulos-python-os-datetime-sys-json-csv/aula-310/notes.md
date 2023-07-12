# http.server - servindo arquivos HTML e CSS via HTTP com um comando Python

Para servir arquivos HTML e CSS via HTTP a partir do terminal usando o módulo http.server, você pode seguir os seguintes passos:

1. Abra o terminal ou prompt de comando no seu sistema operacional.

2. Navegue até o diretório onde os arquivos HTML e CSS estão localizados. Por exemplo, se os arquivos estão em uma pasta chamada "meusite", você pode usar o comando `cd` para entrar nesse diretório:

   ```
   cd meusite
   ```

3. Agora você pode usar o módulo http.server para iniciar um servidor web simples. No Python 3, o módulo está embutido, então você não precisa instalar nada. Basta digitar o seguinte comando no terminal:

   ```
   python -m http.server
   ```

   Caso você queira especificar um diretório contendo os arquivos do seu site, basta usar a opção `-d` seguido do caminho do diretório:

   ```
   python -m http.server -d ./meusite
   ```

4. Após executar o comando, o servidor web será iniciado e começará a servir os arquivos do diretório atual. Ele utilizará a porta 8000 por padrão. Se você desejar usar uma porta diferente, pode especificá-la adicionando o número da porta ao final do comando. Por exemplo, para usar a porta 8080, você pode usar o seguinte comando:

   ```
   python3 -m http.server 8080
   ```

5. Uma vez que o servidor esteja em execução, você pode acessar o seu site abrindo um navegador web e digitando o seguinte URL:

   ```
   http://localhost:8000
   ```

   Se você especificou uma porta diferente, substitua "8000" pelo número da porta que você escolheu.

Esse método é útil para testar sites estáticos ou raspagem de dados (_web scrapping_) localmente, pois o módulo http.server permite que você sirva rapidamente os arquivos HTML e CSS sem precisar configurar um servidor web completo. No entanto, é importante observar que o módulo http.server não é adequado para ambientes de produção ou sites de alto tráfego, pois é um servidor web básico e não escalável.
