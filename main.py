import time
from webbrowser import get
start = time.time()

print("Total de 5 atendimentos. Os exames do atendimento5 estão prontos!")
opcaoEnvio = input('Deseja enviar SMS para os clientes? 1 - Sim ou 2 - Não: ')
numeroOpcao = int(opcaoEnvio)
if (numeroOpcao == 1):
    print("Certo, vamos inciar!")
    atendimento = ['Luiz', '38 anos', 'Exames gerais de laboratório', '49999241385']

    txtMensagem = ('Prezado cliente, os resultados dos seus exames estão disponíveis para retirada.')
    print("Encaminhando SMS para " + atendimento[0] + " fone: " + atendimento[3])
    phone_number = "55" + atendimento[3].get()
    message = txtMensagem.get()
    message_type = "ARN"
    response = message(phone_number, message, message_type)
    if response.status_code == 200:
        sendmsg.showinfo("success","SMS Enviado Com Sucesso")
    else:
        messagebox.showerror("error","Falha ao enviar SMS, Verifique o Numero é tente novamente")
else:
    (numeroOpcao > 2)
    print('[ERRO] Digite uma opção válida!')
    
    print('Não esqueça de enviar os SMS, até mais!')

end = time.time()
# print("Tempo de execução: " + str(end - start))

# atend2 = ['Joana', '20 anos', 'Exames gerais de sangue', '49999241385']
# atend3 = ['Fernanda', '35 anos', 'Exames gerais de urina', '49999257044']
# atend4 = ['Camila', '01 anos', 'Exames gerais de hemoglobina', '49999662588']
# atend5 = ['Evaldo', '15 anos', 'Exames gerais de medula', '49999352145']