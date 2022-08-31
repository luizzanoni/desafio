import time
start = time.time()

print("Total de 5 exames coletados, e 2 exames prontos!")
opcaoEnvio = input('Deseja enviar SMS para os clientes? 1 - Sim ou 2 - Não: ')
numeroOpcao = int(opcaoEnvio)
if (numeroOpcao == 1):
    print("Certo, vamos inciar!")
    atend1 = ['Luiz', '38 anos', 'Exames gerais de laboratório', '49988165833']
    atend2 = ['Joana', '20 anos', 'Exames gerais de sangue', '49999241385']
    atend3 = ['Fernanda', '35 anos', 'Exames gerais de urina', '49999257044']
    atend4 = ['Camila', '01 anos', 'Exames gerais de hemoglobina', '49999662588']
    atend5 = ['Evaldo', '15 anos', 'Exames gerais de medula', '49999352145']

    opcaoMSG1 = str('Prezado cliente, os resultados dos seus exames estão disponíveis para retirada.')
    opcaoMSG2 = str('Prezado cliente, os resultados dos seus exames estão disponíveis para retirada.')
    opcaoEnvioMSG = input('Qual dos SMS deseja enviar? Model 1 ou Model 2?: ')
    if opcaoEnvioMSG == 1:
        print(opcaoMSG1)

    else:
        print(opcaoMSG2)

    sendMSG = atend5[3]
    print("Encaminhando SMS para " + atend5[0] + " fone: " + atend5[3])
else:
    if(numeroOpcao > 2):
        print('[ERRO] Digite uma opção válida!')

    else:
        print('Não esqueça de enviar os SMS, até mais!')

end = time.time()
# print("Tempo de execução: " + str(end - start))

