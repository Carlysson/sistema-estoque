"""Pontos de partida para as funções do Sistema de Gerenciamento de Estoque.

As funções abaixo representam as responsabilidades planejadas para a equipe.
Elas ainda não implementam as operações de estoque. Cada responsável deverá
desenvolver, testar e integrar sua parte conforme o README.md.
"""


def carregar_dados(caminho):
    """Carrega dados de um arquivo JSON.

    TODO: implementar a leitura do arquivo JSON e definir o tratamento de erros.
    Responsável: Carlysson (coordenação da integração) / equipe (contrato comum).
    """
    raise NotImplementedError("Leitura de JSON ainda não implementada.")


def salvar_dados(caminho, dados):
    """Salva dados em um arquivo JSON.

    TODO: implementar a gravação dos dados e definir o tratamento de erros.
    Responsável: Carlysson (coordenação da integração) / equipe (contrato comum).
    """
    raise NotImplementedError("Gravação de JSON ainda não implementada.")


def cadastrar_produto():
    """Solicita e cadastra um novo produto.

    TODO (Paulista): implementar cadastro e validações dos campos.
    """
    raise NotImplementedError("Cadastro de produtos ainda não implementado.")


def listar_produtos():
    """Apresenta os produtos cadastrados.

    TODO (Paulista): implementar a listagem de produtos.
    """
    raise NotImplementedError("Listagem de produtos ainda não implementada.")


def localizar_produto(codigo):
    """Localiza um produto pelo código informado.

    TODO (Paulista): implementar a busca pelo código.
    """
    raise NotImplementedError("Busca de produtos ainda não implementada.")


def registrar_entrada():
    """Registra a entrada de mercadorias no estoque.

    TODO (Paulo): implementar entrada, atualização do saldo e validações.
    """
    raise NotImplementedError("Registro de entrada ainda não implementado.")


def registrar_saida():
    """Registra a saída de mercadorias do estoque.

    TODO (Paulo): implementar saída e validação para impedir saldo negativo.
    """
    raise NotImplementedError("Registro de saída ainda não implementado.")


def registrar_movimentacao(produto, tipo, quantidade, saldo_anterior, saldo_atual):
    """Registra os dados de uma movimentação.

    TODO (Paulo): implementar o registro de entradas e saídas no histórico.
    """
    raise NotImplementedError("Registro de movimentações ainda não implementado.")


def relatorio_estoque_baixo():
    """Apresenta produtos abaixo do estoque mínimo.

    TODO (João Victor): implementar o relatório de estoque mínimo.
    """
    raise NotImplementedError("Relatório de estoque baixo ainda não implementado.")


def calcular_valor_total():
    """Calcula o valor estimado total armazenado.

    TODO (João Victor): implementar o cálculo de preço multiplicado pela quantidade.
    """
    raise NotImplementedError("Cálculo do valor total ainda não implementado.")


def listar_produtos_disponiveis():
    """Apresenta produtos cuja quantidade seja maior que zero.

    TODO (João Victor): implementar o relatório de produtos disponíveis.
    """
    raise NotImplementedError("Relatório de produtos disponíveis ainda não implementado.")


def exibir_historico():
    """Apresenta o histórico de movimentações registradas.

    TODO (João Victor): implementar a consulta e exibição do histórico.
    """
    raise NotImplementedError("Consulta do histórico ainda não implementada.")


def exibir_menu():
    """Apresenta o menu principal e recebe a opção do usuário.

    TODO (Carlysson): implementar o menu e combinar o fluxo com os demais integrantes.
    """
    raise NotImplementedError("Menu principal ainda não implementado.")


def executar():
    """Inicializa a versão-base do projeto sem executar funcionalidades pendentes."""
    print("=" * 54)
    print(" SISTEMA DE GERENCIAMENTO DE ESTOQUE")
    print("=" * 54)
    print("Versão-base do projeto.")
    print("O sistema ainda está em desenvolvimento pela equipe.")
    print("Consulte o README.md para conhecer os requisitos.")
    print("As funcionalidades serão implementadas pelos integrantes.")
