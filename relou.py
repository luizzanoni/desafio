def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        opcaoEnvio = str(input(msg))
        if opcaoEnvio.isnumeric():
            valor = int(opcaoEnvio)
            ok = True
        else:
            print('[ERRO] Digite uma opção válida!')
        if ok:
            break
        return valor

n = leiaInt("Digite")
print("voce acabou {n}")