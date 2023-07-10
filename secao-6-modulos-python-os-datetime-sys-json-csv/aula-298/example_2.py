from string import Template

class MeuTemplate(Template):
    delimiter = '%'  # Define o delimitador para substituições no template

# Exemplo de uso do template personalizado
template = MeuTemplate('Olá, %{nome}! Seu saldo é %{saldo}.')

# Preenche o template com os valores fornecidos
mensagem = template.substitute(nome='João', saldo='R$ 100,00')

print(mensagem)