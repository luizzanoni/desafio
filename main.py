import time
time_duration = 2
start = time.time()

print("Os exames estão prontos!")
opcaoEnvio = input('Deseja enviar SMS para os clientes? 1 - Sim ou 2 - Não: ')
numeroOpcao = int(opcaoEnvio)
if (numeroOpcao == 1):
    print("Enviando...")
    time.sleep(time_duration)
    atendimento = ('Luiz', '38 anos', 'Exames gerais de laboratório', '49999241385')
    len(atendimento)
    nome, idade, exames, telefone = atendimento
    txtMensagem = ('"Prezado cliente, os resultados dos seus exames estão disponíveis para retirada."')
    celular = "55" + telefone
    message = txtMensagem
    response = celular, message
    if response == False:
        print('Falha ao enviar SMS, Verifique o Numero e tente novamente')
    else:
        print('SMS Enviado Com Sucesso para: ' + telefone )
    print(txtMensagem)
else:  
    print('Não esqueça de enviar os SMS, até mais!')
end = time.time()
time.sleep(time_duration)