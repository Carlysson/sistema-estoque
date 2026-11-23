# Imports
import json
import math
import os
from datetime import datetime

# Constantes dos caminhos dos arquivos JSON
ARQUIVO_PRODUTOS = "dados/produtos.json"
ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.json"


def carregar_dados(caminho):
    if not os.path.exists(caminho):
        return []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if isinstance(dados, list):
            return dados

        print(f"Aviso: estrutura inválida em {caminho}.")
        return []

    except (json.JSONDecodeError, OSError):
        print(f"Aviso: não foi possível carregar {caminho}.")
        return []


def salvar_dados(caminho, dados):
    pasta = os.path.dirname(caminho)

    if pasta:
        os.makedirs(pasta, exist_ok=True)

    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    except OSError as erro:
        print(f"Erro ao salvar os dados: {erro}")


def ler_texto_obrigatorio(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: este campo não pode ser vazio.")


def ler_inteiro_nao_negativo(mensagem: str, erro_tipo: str, erro_negativo: str) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor < 0:
                print(erro_negativo)
                continue
            return valor
        except ValueError:
            print(erro_tipo)


def ler_preco(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if not math.isfinite(valor) or valor <= 0:
                print("Erro: o preço deve ser um número finito maior que zero.")
                continue
            return valor
        except ValueError:
            print("Erro: informe um preço numérico válido.")


def cadastrar_produto() -> dict:
    """Solicita e cadastra um novo produto."""

    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    while True:
        codigo = ler_texto_obrigatorio("Código do produto: ")

        if localizar_produto(codigo) is not None:
            print("Erro: esse código já está cadastrado.")
            continue

        break

    nome = ler_texto_obrigatorio("Nome do produto: ")
    preco = ler_preco("Preço do produto: ")

    quantidade = ler_inteiro_nao_negativo(
        "Quantidade inicial: ",
        "Erro: informe uma quantidade inteira válida.",
        "Erro: a quantidade não pode ser negativa.",
    )

    estoque_minimo = ler_inteiro_nao_negativo(
        "Estoque mínimo: ",
        "Erro: informe um número inteiro válido.",
        "Erro: o estoque mínimo não pode ser negativo.",
    )

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "estoque_minimo": estoque_minimo,
    }

    produtos.append(produto)
    salvar_dados(ARQUIVO_PRODUTOS, produtos)

    print("\nProduto cadastrado com sucesso!")

    return produto


def listar_produtos():
    """Exibe todos os produtos cadastrados."""

    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n========== PRODUTOS CADASTRADOS ==========")

    for produto in produtos:
        print(f"\nCódigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Estoque mínimo: {produto['estoque_minimo']}")

    print("\n==========================================")



def localizar_produto(codigo):
    """Localiza um produto pelo código informado."""

    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto

    return None


def ler_quantidade_positiva(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor > 0:
                return valor
            print("Erro: a quantidade deve ser maior que zero.")
        except ValueError:
            print("Erro: informe uma quantidade inteira válida.")


def buscar_na_lista(produtos, codigo):
    """procura o prduto dentro da própia lista que será salva depois"""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def registrar_entrada():
    """Registra a entrada de produtos no estoque."""
    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    codigo = ler_texto_obrigatorio("Código do produto: ")
    produto = buscar_na_lista(produtos, codigo)

    if produto is None:
        print("Erro: produto não encontrado.")
        return

    quantidade = ler_quantidade_positiva("Quantidade a entrar: ")
    saldo_anterior = produto["quantidade"]
    saldo_atual = saldo_anterior + quantidade

    produto["quantidade"] = saldo_atual
    salvar_dados(ARQUIVO_PRODUTOS, produtos)
    registrar_movimentacao(produto, "entrada", quantidade, saldo_anterior, saldo_atual)

    print(f"\nEntrada registrada! Saldo: {saldo_anterior} -> {saldo_atual}")


def registrar_saida():
    """Registra a saída de produtos do estoque."""
    produtos = carregar_dados(ARQUIVO_PRODUTOS)
    codigo = ler_texto_obrigatorio("Código do produto: ")
    produto = buscar_na_lista(produtos, codigo)

    if produto is None:
        print("Erro: produto não encontrado.")
        return

    quantidade = ler_quantidade_positiva("Quantidade a sair: ")
    saldo_anterior = produto["quantidade"]

    if quantidade > saldo_anterior:
        print(f"Erro: quantidade insuficiente em estoque. Saldo disponível: {saldo_anterior}.")
        return

    saldo_atual = saldo_anterior - quantidade
    produto["quantidade"] = saldo_atual
    salvar_dados(ARQUIVO_PRODUTOS, produtos)
    registrar_movimentacao(produto, "saida", quantidade, saldo_anterior, saldo_atual)

    print(f"\nSaída registrada! Saldo: {saldo_anterior} -> {saldo_atual}")


def registrar_movimentacao(produto, tipo, quantidade, saldo_anterior, saldo_atual):
    """Registra uma movimentação de entrada ou saída no histórico."""
    movimentacoes = carregar_dados(ARQUIVO_MOVIMENTACOES)

    movimentacao = {
        "codigo": produto["codigo"],
        "nome": produto["nome"],
        "tipo": tipo,
        "quantidade": quantidade,
        "saldo_anterior": saldo_anterior,
        "saldo_atual": saldo_atual,
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    movimentacoes.append(movimentacao)
    salvar_dados(ARQUIVO_MOVIMENTACOES, movimentacoes)


def relatorio_estoque_baixo():
    """Apresenta produtos abaixo do estoque mínimo."""

    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    print("\n" + "=" * 62)
    print(" PRODUTOS ABAIXO DO ESTOQUE MÍNIMO")
    print("=" * 62)

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'Código':<8}{'Nome':<24}{'Qtd':>6}{'Mínimo':>8}{'Falta':>7}")
    print("-" * 62)

    encontrados = 0

    for produto in produtos:
        if produto["quantidade"] < produto["estoque_minimo"]:
            falta = produto["estoque_minimo"] - produto["quantidade"]
            print(
                f"{produto['codigo']:<8}{produto['nome']:<24}"
                f"{produto['quantidade']:>6}{produto['estoque_minimo']:>8}{falta:>7}")
            
            encontrados = encontrados + 1

    print("-" * 62)
    if encontrados == 0:
        print("Nenhum produto abaixo do estoque mínimo.")
    else:
        print(f"Total de produtos abaixo do mínimo: {encontrados}")


def calcular_valor_total():

    """Calcula o valor estimado total armazenado."""

    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    valor_total = 0.0 # acumulador: começa em 0

    print("\n" + "=" * 62)
    print(" VALOR TOTAL ARMAZENADO NO ESTOQUE ")
    print("=" * 62)

    if len(produtos) == 0:
        print(" Nenhum produto cadastrado ")
        print(f" Valor total estimado: R$ {valor_total:.2f}")
        
        return valor_total

    print(f"{'Código':<8}{'Nome':<24}{'Qtd':>6}{'Preço':>11}{'Subtotal':>13}")
    print("-" * 62)

    for produto in produtos:
        
        subtotal = produto["preco"] * produto["quantidade"]
        
        valor_total = valor_total + subtotal
        
        print(
            f"{produto['codigo']:<8}{produto['nome']:<24}{produto['quantidade']:>6}"
            f"{'R$ ' + format(produto['preco'], '.2f'):>11}"
            f"{'R$ ' + format(subtotal, '.2f'):>13}")

    print("-" * 62)
    print(f"Valor total estimado: R$ {valor_total:.2f}")
    
    return valor_total


def listar_produtos_disponiveis():
    """Apresenta produtos cuja quantidade seja maior que zero."""

    produtos = carregar_dados(ARQUIVO_PRODUTOS)

    print("\n" + "=" * 62)
    print(" PRODUTOS DISPONÍVEIS EM ESTOQUE")
    print("=" * 62)

    if len(produtos) ==0:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'Código':<8}{'Nome':<24}{'Qtd':>6}{'Preço':>12}")
    print("-" * 62)

    disponiveis = 0

    for produto in produtos:
        if produto["quantidade"] > 0:
            print(
                f"{produto['codigo']:<8}{produto['nome']:<24}{produto['quantidade']:>6}"
                f"{'R$ ' + format(produto['preco'], '.2f'):>12}"
            )
            disponiveis = disponiveis + 1


    print("-" * 62)
    if disponiveis == 0:
        print("Nenhum produto disponível em estoque.")
    else:
        print(f"Total de produtos disponíveis: {disponiveis}")


def exibir_historico():
    """Apresenta o histórico de movimentações registradas."""
    
    movimentacoes = carregar_dados(ARQUIVO_MOVIMENTACOES)

    print("\n" + "=" * 86)
    print(" HISTÓRICO DE MOVIMENTAÇÕES")
    print("=" * 86)

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")
        return

    print(
        f"{'Data/hora':<21}{'Tipo':<9}{'Código':<8}{'Produto':<20}"
        f"{'Qtd':>5}{'Anterior':>10}{'Atual':>8}"
    )
    print("-" * 86)

    for mov in reversed(movimentacoes):
        try:
            data = datetime.fromisoformat(mov["data_hora"]).strftime("%d/%m/%Y %H:%M:%S")
        except ValueError:
            data = mov["data_hora"]


        if mov["tipo"] == "entrada":
            tipo = "Entrada"
        elif mov["tipo"] in ("saida", "saída"):
            tipo = "Saída"
        else:
            tipo = mov["tipo"]  
        print(
            f"{data:<21}{tipo:<9}{mov['codigo']:<8}{mov['nome']:<20}"
            f"{mov['quantidade']:>5}{mov['saldo_anterior']:>10}{mov['saldo_atual']:>8}"
        )

    print("-" * 86)
    print(f"Total de movimentações: {len(movimentacoes)}")


def exibir_menu():
    """Apresenta o menu principal e recebe a opção do usuário."""

    print("\n" + "=" * 54)
    print("       SISTEMA DE GERENCIAMENTO DE ESTOQUE")
    print("=" * 54)
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Relatório de estoque baixo")
    print("6 - Calcular valor total do estoque")
    print("7 - Listar produtos disponíveis")
    print("8 - Exibir histórico de movimentações")
    print("0 - Sair")
    print("=" * 54)

    return input("Escolha uma opção: ").strip()


def executar():
    """Executa o fluxo principal do sistema."""

    print("\nBem-vindo ao Sistema de Gerenciamento de Estoque!")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            registrar_entrada()

        elif opcao == "4":
            registrar_saida()

        elif opcao == "5":
            relatorio_estoque_baixo()

        elif opcao == "6":
            calcular_valor_total()

        elif opcao == "7":
            listar_produtos_disponiveis()

        elif opcao == "8":
            exibir_historico()

        elif opcao == "0":
            print("\nEncerrando o sistema. Até mais!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")