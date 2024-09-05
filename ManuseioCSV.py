import datetime

inventario = {}

while True:
    opcao = int(input(
        "Digite: \n"
        "<1> para registrar ativo\n"
        "<2> para persistir em arquivo\n"
        "<3> para exibir ativos armazenados: "
    ))

    if opcao == 1:
        resp = "S"
        while resp == "S":
            numero_patrimonial = input("Digite o número patrimonial: ")
            data = datetime.datetime.now().strftime("%d/%m/%Y")
            descricao = input("Digite a descrição: ")
            departamento = input("Digite o departamento: ")
            inventario[numero_patrimonial] = [
                data,
                descricao,
                departamento
            ]
            resp = input("Digite <S> para continuar ou qualquer outra tecla para parar: ").upper()

    elif opcao == 2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(f"{chave};{valor[0]};{valor[1]};{valor[2]}\n")
        print("Persistido com sucesso!")

    elif opcao == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.read())

    else:
        print("Opção inválida. Tente novamente.")
