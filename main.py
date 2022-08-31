# Powered by: Luiz Gustavo Zanoni
# Date: 31/08/2022

import time
timeDuration = 2

print("Os exames estão prontos!")
opcaoEnvio = input('Deseja enviar SMS para os clientes? 1 - Sim ou 2 - Não:\n ')
numeroOpcao = int(opcaoEnvio)
if (numeroOpcao == 1):
    # array simulando um banco de dados, soldado dentro do código
    atendimento = ('Luiz', '38 anos', 'Exames gerais de laboratório', '49999241385')
    nome, idade, exames, telefone = atendimento
    txtMensagem = ('"Prezado cliente, os resultados dos seus exames estão disponíveis para retirada."')
    # mini "API" de como ele pegaria os dados e encaminharia ao contato salvo
    celular = "55" + telefone
    message = txtMensagem
    response = celular, message
    # faz a verificação de algum dado, caso for falso ou nulo, ele gera falha de envio
    print("Enviando...")
    time.sleep(timeDuration) # simulando uma pausa para enviar a mensagem
    if response == False:
        print('Falha ao enviar SMS, Verifique o Numero e tente novamente')
    else:
        print('SMS enviado com sucesso para ' + nome + ' no telefone: ' + telefone )
    print(txtMensagem)
    # caso não queira executar o código, ou aguardar, ele tem uma saída
else:
    print('Não esqueça de enviar os SMS, até mais!')
end = time.time()
time.sleep(timeDuration)