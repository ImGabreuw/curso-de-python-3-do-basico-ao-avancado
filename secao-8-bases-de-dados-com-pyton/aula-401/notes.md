# Criando um .env para evitar enviar senhas e dados sensíveis para o Github

O arquivo `.env` é usado no contexto do docker-compose para armazenar variáveis de ambiente que podem ser usadas em um arquivo `docker-compose.yml`. Ele permite que você defina valores de configuração dinamicamente e os substitua facilmente sem modificar o arquivo `docker-compose.yml` diretamente.

Aqui está um exemplo de como usar o arquivo `.env` com o docker-compose:

1. Crie um arquivo chamado `.env` no mesmo diretório do arquivo `docker-compose.yml`.

2. Dentro do arquivo `.env`, você pode definir as variáveis de ambiente no formato `VARIAVEL=valor`. Por exemplo:

```
MYSQL_ROOT_PASSWORD=senha
MYSQL_DATABASE=base_de_dados
MYSQL_USER=usuario
MYSQL_PASSWORD=senha
```

3. No arquivo `docker-compose.yml`, você pode carregar essas variáveis de ambientes declaradas no arquivo `.env` com a propriedade `env_file`. Por exemplo:

```yaml
version: "3.9"
services:
  mysql_206:
    env_file:
      - .env
    container_name: mysql_206
    hostname: mysql_206
    image: mysql:8
    restart: always
    command:
      - --authentication-policy=mysql_native_password
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
      - --innodb_force_recovery=0
    volumes:
      - ./mysql_206:/var/lib/mysql
    ports:
      - 3306:3306
    environment:
      TZ: America/Sao_Paulo
```

Dessa forma, você pode gerenciar facilmente as configurações do seu ambiente usando variáveis de ambiente no arquivo `.env`, sem precisar modificar diretamente o arquivo `docker-compose.yml`. Isso torna mais conveniente configurar diferentes ambientes (por exemplo, desenvolvimento, teste, produção) com diferentes valores de variáveis de ambiente.O arquivo `.env` é usado no contexto do docker-compose para armazenar variáveis de ambiente que podem ser usadas em um arquivo `docker-compose.yml`. Ele permite que você defina valores de configuração dinamicamente e os substitua facilmente sem modificar o arquivo `docker-compose.yml` diretamente.
