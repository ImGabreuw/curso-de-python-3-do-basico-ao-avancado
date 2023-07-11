# Configurando o SMTP e senhas de apps no GMAIL para enviar e-mails com Python

Para configurar o SMTP (Simple Mail Transfer Protocol) e utilizar senhas de aplicativos no Gmail para enviar e-mails usando Python, você precisará seguir algumas etapas.

Passo 1: Habilitar o acesso ao SMTP no Gmail

1. Faça login na sua conta do Gmail.

2. Acesse as configurações da conta clicando no ícone de engrenagem no canto superior direito e selecionando "Configurações".

3. Vá para a guia "Encaminhamento e POP/IMAP".

4. Na seção "Acesso IMAP", selecione "Ativar IMAP".

5. Role para baixo até a seção "Acesso a apps menos seguros" e habilite essa opção. Isso permitirá que você se autentique usando o SMTP em seu aplicativo Python.

Passo 2: crie uma senha de aplicativo do Gmail

1. Pesquise no Google por `Senhas de app Gmail`

2. Acesse o site [Ajuda da Conta do Google](https://support.google.com/accounts/answer/185833?hl=pt-BR)

3. Siga o passo a passo para criar a senha de aplicativo

Passo 3: Instalar a biblioteca 'smtplib' do Python

1. Certifique-se de ter o Python instalado em seu computador.

2. Abra o terminal ou prompt de comando e execute o seguinte comando para instalar a biblioteca 'smtplib':

   ```
   pip install secure-smtplib
   ```

Passo 4: Escrever o código Python para enviar e-mails

Aqui está um exemplo de código Python que utiliza a biblioteca 'smtplib' para enviar um e-mail usando o SMTP do Gmail:

No código fornecido, a parte relacionada ao SMTP é a seguinte:

```python
# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')
```

Nesta seção, você está configurando o servidor SMTP, portas e informações de autenticação para enviar o e-mail.

- `smtp_server`: É definido como `'smtp.gmail.com'`, que é o servidor SMTP do Gmail.
- `smtp_port`: É definido como `587`, que é a porta padrão para comunicações SMTP.
- `smtp_username`: É atribuído ao valor de `os.getenv('FROM_EMAIL', '')`, que obtém o endereço de e-mail do remetente a partir de uma variável de ambiente chamada `'FROM_EMAIL'`. Esse valor é necessário para autenticação no servidor SMTP.
- `smtp_password`: É atribuído ao valor de `os.getenv('EMAIL_PASSWORD', '')`, que obtém a senha de e-mail do remetente a partir de uma variável de ambiente chamada `'EMAIL_PASSWORD'`. Essa senha é necessária para autenticação no servidor SMTP.

Em seguida, a parte do código que envia o e-mail começa com:

```python
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')
```

- `smtplib.SMTP(smtp_server, smtp_port)`: Cria uma conexão com o servidor SMTP usando o endereço do servidor e a porta fornecidos.
- `server.ehlo()`: Executa o "ehlo" (hello extendido) para iniciar a comunicação com o servidor SMTP.
- `server.starttls()`: Inicia uma conexão TLS (Transport Layer Security) para criptografar a comunicação entre o cliente e o servidor SMTP.
- `server.login(smtp_username, smtp_password)`: Realiza a autenticação no servidor SMTP usando o nome de usuário (endereço de e-mail) e a senha fornecidos.
- `server.send_message(mime_multipart)`: Envia a mensagem de e-mail, que foi preparada anteriormente como um objeto `MIMEMultipart`, usando o servidor SMTP autenticado.

Lembre-se de que o Gmail possui restrições de envio de e-mails em grandes quantidades para evitar abusos. Portanto, é importante verificar as políticas de uso do Gmail para garantir o envio adequado de e-mails em seu aplicativo Python.
