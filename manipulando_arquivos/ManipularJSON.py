import json
import datetime

def obter_data_atual():
    """Retorna a data atual formatada como 'dd/mm/aaaa'"""
    return datetime.datetime.now().strftime("%d/%m/%Y")

inventario = {}

while True:
    opcao = int(input(
        "Digite: \n"
        "<1> para registrar ativo\n"
        "<2> para exibir ativos armazenados\n"
        "<3> para sair\n"
    ))

    if opcao == 1:
        resp = "S"
        while resp == "S":
            numero_patrimonial = input("Digite o número patrimonial: ")
            descricao = input("Digite a descrição: ")
            departamento = input("Digite o departamento: ")
            data_atual = obter_data_atual()
            inventario[numero_patrimonial] = [descricao, departamento, data_atual]
            resp = input("Digite <S> para continuar ou qualquer outra tecla para parar: ").upper()
        
        with open("./arquivos/inventario.json", "w") as arq_json:
            json.dump(inventario, arq_json, indent=4)
        print("JSON Gerado!")

    elif opcao == 2:
        try:
            with open("./arquivos/inventario.json", "r") as arq_json:
                resultado = json.load(arq_json)
                for x, y in resultado.items():
                    print("Número Patrimonial: ", x)
                    print("Data: ", y[2])
                    print("Descrição: ", y[0])
                    print("Departamento: ", y[1])
                    print("-" * 20)  # Linha separadora para clareza
        except FileNotFoundError:
            print("Arquivo 'inventario.json' não encontrado.")

    elif opcao == 3:
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
