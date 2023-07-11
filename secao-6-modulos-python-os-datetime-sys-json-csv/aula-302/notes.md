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

```python
import smtplib
from email.mime.text import MIMEText

# Configurações do servidor SMTP do Gmail
smtp_host = 'smtp.gmail.com'
smtp_port = 587

# Seu endereço de e-mail e senha de aplicativo
sender_email = 'seu_email@gmail.com'
app_password = 'sua_senha_de_aplicativo'

# Destinatário do e-mail
recipient_email = 'destinatario@example.com'

# Criação da mensagem de e-mail
message = MIMEText('Olá, este é um e-mail de teste enviado pelo Python!')
message['Subject'] = 'E-mail de teste'
message['From'] = sender_email
message['To'] = recipient_email

# Conexão e autenticação com o servidor SMTP
smtp_server = smtplib.SMTP(smtp_host, smtp_port)
smtp_server.starttls()
smtp_server.login(sender_email, app_password)

# Envio do e-mail
smtp_server.send_message(message)

# Encerramento da conexão com o servidor SMTP
smtp_server.quit()
```

Certifique-se de substituir `'seu_email@gmail.com'` pelo seu próprio endereço de e-mail e `'sua_senha_de_aplicativo'` pela senha de aplicativo gerada pelo Gmail.

Esse código estabelece uma conexão com o servidor SMTP do Gmail, autentica-se usando seu endereço de e-mail e senha de aplicativo, cria uma mensagem de e-mail e a envia para o destinatário especificado.

Lembre-se de que o Gmail possui restrições de envio de e-mails em grandes quantidades para evitar abusos. Portanto, é importante verificar as políticas de uso do Gmail para garantir o envio adequado de e-mails em seu aplicativo Python.
