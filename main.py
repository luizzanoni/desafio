import time
start = time.time()

print("Total de 15 exames coletados, e 7 exames prontos!")
opcaoEnvio = input('Deseja enviar SMS para os clientes? 1 - Sim ou 2 - Não: ')
numeroOpcao = int(opcaoEnvio)
if (numeroOpcao == 1):
    print("Encaminhando os SMS!")
    exame1 = ['Luiz', '28 anos', 'Exames gerais de laboratório', '49999999999']

else:
    if(numeroOpcao > 2):
        print('[ERRO] Digite uma opção válida!')

    else:
        print('Não esqueça de enviar os SMS, até mais!')

end = time.time()
print("Tempo de execução em segundos: " + str(end - start))









examePronto = ['Luiz', '28 anos', 'Exames gerais de laboratório', '49999999999']
# print (examePronto)
