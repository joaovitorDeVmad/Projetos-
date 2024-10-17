
# importa base de dados
import pandas as pd
tabela_vendas = pd.read_excel('Vendas.xlsx')
print(tabela_vendas)
# visualizar base de dados
pd.set_option('display.max_columns' , None)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja' , 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-'* 50)
# ticket medio por produto em cada loja
ticketmedio = (faturamento['Valor Final'] / quantidade [ 'Quantidade']).to_frame()
print(ticketmedio)

# enviar email com resultado
import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>prezados</p>
    <p>esse e o teste do email automático</p>
    <p>joao vitor almeida</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "teste"
    msg['From'] = 'seu email'
    msg['To'] = 'seu email'
    password = 'sua senha'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# devido as novas politicas de segurança esse metodo nao funciona mais