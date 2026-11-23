# Sistema de Gerenciamento de Estoque

Projeto acadêmico desenvolvido em **Python 3**, com interface de terminal e armazenamento local em arquivos JSON. O sistema tem como objetivo auxiliar no controle de mercadorias de pequenos comércios e aplicar os conceitos de **programação imperativa**, por meio de uma organização procedural baseada em funções.

O projeto permite cadastrar produtos, consultar o estoque, registrar entradas e saídas, gerar relatórios e consultar o histórico de movimentações.

---

## 1. Objetivo e problema

O controle manual de mercadorias pode provocar divergências entre a quantidade registrada e a quantidade realmente disponível. Também pode dificultar a identificação de produtos com estoque baixo, atrasar consultas e tornar trabalhoso estimar o valor armazenado.

O Sistema de Gerenciamento de Estoque propõe uma solução simples para esse problema, reunindo as principais operações em um programa executado pelo terminal.

Além de solucionar uma necessidade prática, o objetivo acadêmico é aplicar os conceitos de programação imperativa em Python, utilizando variáveis, atribuições, estruturas condicionais, estruturas de repetição, funções e manipulação de dados.

## 2. Funcionalidades implementadas

O sistema possui as seguintes funcionalidades:

1. **Cadastro de produtos:** registra código, nome, preço, quantidade inicial e estoque mínimo.
2. **Validação cadastral:** impede códigos duplicados e solicita novamente os campos obrigatórios quando estão vazios ou inválidos.
3. **Listagem de produtos:** apresenta os produtos cadastrados e suas informações.
4. **Localização de produtos:** permite localizar um produto pelo código.
5. **Entrada de mercadorias:** registra o recebimento de determinada quantidade de um produto.
6. **Saída de mercadorias:** registra a retirada de determinada quantidade.
7. **Atualização do estoque:** atualiza automaticamente a quantidade disponível após cada entrada ou saída.
8. **Validação de saída:** impede retiradas superiores ao saldo disponível.
9. **Relatório de estoque baixo:** identifica produtos cuja quantidade esteja abaixo do estoque mínimo definido.
10. **Cálculo do valor total:** estima o valor armazenado utilizando preço unitário × quantidade disponível.
11. **Relatório de produtos disponíveis:** apresenta produtos cuja quantidade seja maior que zero.
12. **Histórico de movimentações:** apresenta data e hora, tipo de operação, produto, quantidade movimentada e saldos anterior e atual.
13. **Persistência em JSON:** salva e recupera os cadastros e as movimentações em arquivos locais.
14. **Menu principal:** permite acessar as funcionalidades e encerrar o programa por meio da opção 0.

## 3. Requisitos e ferramentas

| Item | Requisito |
|---|---|
| Linguagem | Python 3 |
| Versão recomendada | Python 3.10 ou superior |
| Interface | Terminal/console |
| Armazenamento | Arquivos JSON locais |
| Paradigma | Programação imperativa |
| Organização | Programação procedural por funções |
| Versionamento | Git e GitHub |
| Bibliotecas externas | Nenhuma necessária |

O projeto utiliza módulos da biblioteca padrão do Python, como `json`, `os`, `math` e `datetime`.

Não é necessário instalar banco de dados ou bibliotecas externas para executar a versão atual.

## 4. Como executar o sistema

### Pré-requisitos

- Python 3 instalado.
- Git instalado, caso opte por clonar o repositório.
- Terminal, Prompt de Comando, PowerShell ou terminal integrado de uma IDE.

### Clonando o repositório

Execute:

```bash
git clone https://github.com/Carlysson/sistema-estoque.git
```

Entre na pasta:

```bash
cd sistema-estoque
```

### Executando o programa

Na pasta raiz do projeto, onde está localizado o arquivo `main.py`, execute:

```bash
python main.py
```

Dependendo da instalação do Python, também poderá ser necessário utilizar:

```bash
python3 main.py
```

No Windows:

```bash
py main.py
```

### Utilização

Após a inicialização, o programa apresenta o menu principal:

```text
======================================================
       SISTEMA DE GERENCIAMENTO DE ESTOQUE
======================================================
1 - Cadastrar produto
2 - Listar produtos
3 - Registrar entrada
4 - Registrar saída
5 - Relatório de estoque baixo
6 - Calcular valor total do estoque
7 - Listar produtos disponíveis
8 - Exibir histórico de movimentações
0 - Sair
======================================================
```

O usuário seleciona a operação digitando o número correspondente.

Após a execução de uma operação, o sistema solicita que o usuário pressione ENTER para retornar ao menu. A opção 0 encerra o programa.

## 5. Estrutura do repositório

```text
sistema-estoque/
│
├── main.py
├── estoque.py
├── README.md
├── .gitignore
│
├── dados/
│   ├── produtos.json
│   ├── movimentacoes.json
│   └── .gitkeep
│
├── documentos/
│   ├── README_DOCUMENTACAO.md
│   └── (PDF final do projeto)
│
└── evidencias/
    ├── README_EVIDENCIAS.md
    └── (capturas de tela dos testes)
```

### Finalidade dos arquivos e diretórios

| Caminho | Finalidade |
|---|---|
| `main.py` | Ponto de entrada do sistema. Importa e executa a função principal. |
| `estoque.py` | Arquivo central, contendo as funções de cadastro, movimentação, relatórios, histórico, persistência e menu. |
| `README.md` | Documentação principal do projeto. |
| `.gitignore` | Evita versionar arquivos temporários e configurações locais desnecessárias. |
| `dados/produtos.json` | Armazena os produtos cadastrados e seus saldos atuais. |
| `dados/movimentacoes.json` | Armazena o histórico de entradas e saídas. |
| `dados/.gitkeep` | Mantém a pasta de dados no controle de versão quando necessário. |
| `documentos/` | Diretório destinado à documentação final em PDF e suas orientações. |
| `evidencias/` | Diretório destinado às capturas de tela reais da execução e dos testes. |

### Arquivos JSON

Os dados são armazenados localmente em dois arquivos:

- `produtos.json`: contém a lista de produtos cadastrados.
- `movimentacoes.json`: contém a lista de movimentações realizadas.

Quando não existem registros, a estrutura esperada é uma lista vazia:

```json
[]
```

O programa utiliza as rotinas de carregamento e gravação para consultar e atualizar essas informações.

## 6. Paradigma imperativo: conceitos no código

O projeto foi desenvolvido utilizando o **paradigma imperativo**, que descreve a solução por meio de instruções executadas passo a passo.

A organização é procedural, com funções responsáveis por tarefas específicas e estruturas simples do Python, como listas e dicionários.

A seguir estão os principais conceitos imperativos identificados no código.

### 6.1 Variáveis e atribuições

Variáveis armazenam valores utilizados durante a execução. A atribuição associa um valor a um nome e permite atualizar esse valor conforme as operações realizadas.

Exemplo presente na movimentação de estoque:

```python
saldo_anterior = produto["quantidade"]
saldo_atual = saldo_anterior + quantidade

produto["quantidade"] = saldo_atual
```

O programa utiliza variáveis para armazenar o saldo anterior, a quantidade movimentada e o saldo atualizado.

### 6.2 Condicionais (`if`, `elif` e `else`)

As estruturas condicionais permitem escolher quais instruções serão executadas de acordo com determinada condição.

Exemplo da validação de saída:

```python
if quantidade > saldo_anterior:
    print("Erro: quantidade insuficiente em estoque.")
    return
```

Essa condição impede que o usuário retire uma quantidade superior à disponível.

As condicionais também são utilizadas nas validações cadastrais e na seleção das opções do menu.

### 6.3 Estruturas de repetição (`while` e `for`)

As estruturas de repetição permitem executar instruções várias vezes.

O `while` é utilizado para manter o menu em funcionamento:

```python
while True:
    opcao = exibir_menu()

    if opcao == "0":
        break
```

O `for` é utilizado para percorrer os produtos cadastrados e realizar consultas:

```python
for produto in produtos:
    if produto["quantidade"] > 0:
        print(produto["nome"])
```

### 6.4 Funções e procedimentos

As funções agrupam instruções relacionadas a uma tarefa e organizam o programa em partes menores.

Alguns exemplos presentes no projeto:

- `cadastrar_produto()`
- `listar_produtos()`
- `registrar_entrada()`
- `registrar_saida()`
- `relatorio_estoque_baixo()`
- `calcular_valor_total()`
- `exibir_historico()`
- `carregar_dados()`
- `salvar_dados()`
- `exibir_menu()`
- `executar()`

Cada função possui uma responsabilidade específica, facilitando a organização, manutenção e compreensão do código.

### 6.5 Sequência de comandos

A sequência representa a ordem em que as instruções são executadas.

Durante uma saída de mercadoria, por exemplo, o programa:

1. Carrega os produtos.
2. Solicita o código do produto.
3. Localiza o produto informado.
4. Solicita a quantidade desejada.
5. Verifica se existe saldo suficiente.
6. Atualiza a quantidade disponível.
7. Salva os dados atualizados.
8. Registra a movimentação no histórico.

Essa ordem garante que as operações sejam realizadas de maneira organizada.

A utilização desses conceitos demonstra a aplicação prática da programação imperativa em Python.

## 7. Divisão de responsabilidades

A equipe organizou o desenvolvimento de acordo com as seguintes responsabilidades:

| Integrante | Responsabilidade principal | Atividades |
|---|---|---|
| **Carlysson** | Coordenação e integração | Organização do repositório, integração e revisão das alterações, persistência JSON, menu, fluxo principal e consolidação da documentação. |
| **João Victor** | Relatórios e históricos | Relatório de estoque mínimo, cálculo do valor total, relatório de produtos disponíveis, exibição do histórico e conferência dos resultados. |
| **Paulo** | Entradas e saídas | Registro de entradas e saídas, atualização de quantidades, bloqueio de retiradas acima do saldo e registro das movimentações. |
| **Paulista** | Cadastro e listagem | Cadastro, listagem, localização de produtos e validações cadastrais, como códigos duplicados e campos inválidos. |

### Combinados da equipe

- Cada integrante deve conhecer e conseguir explicar o funcionamento geral do sistema.
- Alterações que afetem outras partes do código devem ser comunicadas aos demais integrantes.
- Mudanças nas assinaturas das funções compartilhadas devem ser combinadas previamente.
- Os commits devem descrever as alterações realmente realizadas.
- O código deve ser testado antes de sua integração à versão compartilhada.
- A integração deve preservar o contrato de dados definido pela equipe.

### Integração em `estoque.py`

As funcionalidades estão organizadas principalmente no arquivo `estoque.py`.

Para evitar conflitos, os integrantes combinaram os nomes das funções, os parâmetros e a estrutura dos dados utilizados.

Paulo é responsável por registrar as movimentações, enquanto João Victor é responsável por consultar e apresentar o histórico dessas operações.

### 7.1 Contrato de dados e funções

Todos os integrantes devem respeitar a estrutura de dados compartilhada.

#### Arquivos

| Arquivo | Conteúdo |
|---|---|
| `dados/produtos.json` | Lista de produtos. |
| `dados/movimentacoes.json` | Lista de movimentações, da mais antiga para a mais recente. |

Os caminhos são definidos por constantes em `estoque.py`:

```python
ARQUIVO_PRODUTOS = "dados/produtos.json"
ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.json"
```

#### Produto

Cada produto é representado por um dicionário com a seguinte estrutura:

```json
{
    "codigo": "001",
    "nome": "Arroz 5kg",
    "preco": 25.90,
    "quantidade": 10,
    "estoque_minimo": 5
}
```

| Campo | Tipo | Regra |
|---|---|---|
| `codigo` | `str` | Único e não vazio. |
| `nome` | `str` | Não vazio. |
| `preco` | `float` | Número finito maior que zero. |
| `quantidade` | `int` | Maior ou igual a zero. |
| `estoque_minimo` | `int` | Maior ou igual a zero. |

O código é armazenado como texto para preservar possíveis zeros à esquerda.

#### Movimentação

Cada movimentação é representada por um dicionário:

```json
{
    "data_hora": "18/11/2026 21:30:05",
    "tipo": "entrada",
    "codigo": "001",
    "nome": "Arroz 5kg",
    "quantidade": 5,
    "saldo_anterior": 10,
    "saldo_atual": 15
}
```

| Campo | Tipo | Regra |
|---|---|---|
| `data_hora` | `str` | Formato `%d/%m/%Y %H:%M:%S`. |
| `tipo` | `str` | `entrada` ou `saida`. |
| `codigo` | `str` | Código do produto movimentado. |
| `nome` | `str` | Nome do produto no momento da operação. |
| `quantidade` | `int` | Quantidade movimentada, maior que zero. |
| `saldo_anterior` | `int` | Saldo antes da operação. |
| `saldo_atual` | `int` | Saldo após a operação. |

#### Funções compartilhadas

| Função | Responsabilidade | Descrição |
|---|---|---|
| `carregar_dados(caminho)` | Carlysson | Carrega uma lista a partir de um arquivo JSON. |
| `salvar_dados(caminho, dados)` | Carlysson | Grava uma lista em arquivo JSON. |
| `localizar_produto(codigo)` | Paulista | Retorna o produto encontrado ou `None`. |
| `registrar_movimentacao(produto, tipo, quantidade, saldo_anterior, saldo_atual)` | Paulo | Registra e salva uma movimentação. |

#### Regras gerais

- As funções que alteram os produtos devem salvar os dados atualizados em `produtos.json`.
- As movimentações devem ser registradas em `movimentacoes.json`.
- As funções de relatório e histórico consultam os dados, sem alterar o estoque.
- Um produto está abaixo do mínimo quando `quantidade < estoque_minimo`.
- Um produto está disponível quando `quantidade > 0`.
- Os valores monetários são exibidos com duas casas decimais.
- As entradas de dados devem tratar valores inválidos e permitir nova tentativa.
- Uma saída superior ao saldo disponível deve ser recusada.

## 8. Roteiro de testes

Os cenários abaixo devem ser utilizados para validar o funcionamento do sistema integrado.

| Cenário | Ação | Resultado esperado |
|---|---|---|
| Inicialização | Executar `python main.py`. | Menu principal apresentado sem erros. |
| Opção inválida | Informar uma opção inexistente. | Mensagem de opção inválida e retorno ao menu. |
| Encerramento | Selecionar a opção `0`. | Programa encerrado corretamente. |
| Cadastro correto | Inserir código novo e dados válidos. | Produto cadastrado e salvo. |
| Código duplicado | Repetir um código existente. | Cadastro recusado. |
| Campo vazio | Não informar um campo obrigatório. | Solicitação de novo valor. |
| Preço inválido | Informar texto, zero ou número negativo. | Solicitação de preço válido. |
| Entrada | Registrar entrada em produto existente. | Saldo aumentado e movimentação registrada. |
| Saída válida | Retirar quantidade disponível. | Saldo diminuído e movimentação registrada. |
| Saída excessiva | Retirar mais que o saldo. | Operação bloqueada e saldo preservado. |
| Código inexistente | Movimentar produto não cadastrado. | Mensagem de produto não encontrado. |
| Estoque mínimo | Consultar produto abaixo do mínimo. | Produto apresentado no relatório. |
| Valor total | Consultar o valor armazenado. | Soma de preço × quantidade de todos os produtos. |
| Produtos disponíveis | Consultar produtos com saldo positivo. | Apenas produtos com quantidade maior que zero são apresentados. |
| Histórico | Consultar movimentações realizadas. | Dados das operações apresentados corretamente. |
| Persistência | Fechar e abrir novamente o programa. | Cadastros e histórico permanecem gravados. |

Os resultados dos testes devem ser registrados pela equipe após a execução real. Um cenário não deve ser considerado aprovado apenas por estar previsto neste roteiro.

## 9. Evidências e documento PDF

As capturas de tela devem ser salvas no diretório `evidencias/`.

Recomenda-se organizar os arquivos com nomes claros:

```text
evidencias/
├── README_EVIDENCIAS.md
├── 01-menu-principal.png
├── 02-cadastro-produto.png
├── 03-listagem-produtos.png
├── 04-registro-entrada.png
├── 05-registro-saida.png
├── 06-bloqueio-estoque-insuficiente.png
├── 07-relatorio-estoque-baixo.png
├── 08-valor-total-estoque.png
├── 09-produtos-disponiveis.png
├── 10-historico-movimentacoes.png
└── 11-persistencia-json.png
```

As imagens devem ser capturas reais da execução do programa, com informações legíveis e correspondentes à versão final do código.

### Estrutura recomendada para o PDF

1. **Capa:** instituição, disciplina, professor e nomes completos dos integrantes.
2. **Introdução:** apresentação do problema e objetivo do projeto.
3. **Requisitos:** descrição dos requisitos funcionais e não funcionais.
4. **Tecnologias:** Python, JSON, Git e GitHub.
5. **Organização do código:** estrutura dos arquivos e responsabilidades das funções.
6. **Paradigma imperativo:** explicação de pelo menos três conceitos demonstrados com exemplos reais do código.
7. **Funcionalidades:** descrição das operações implementadas.
8. **Persistência:** explicação de como os arquivos JSON armazenam os dados.
9. **Testes:** cenários executados, resultados e eventuais correções.
10. **Evidências:** capturas de tela que comprovem o funcionamento.
11. **Equipe:** divisão de responsabilidades.
12. **Conclusão:** resultados alcançados, dificuldades e possíveis melhorias.

O PDF final deverá ser colocado no diretório `documentos/`.

## 10. Git e GitHub

O projeto é versionado por meio do Git e hospedado no GitHub.

Repositório:

https://github.com/Carlysson/sistema-estoque

### Clonar o repositório

```bash
git clone https://github.com/Carlysson/sistema-estoque.git
```

### Atualizar a cópia local

Antes de começar uma nova tarefa, atualize sua cópia conforme o fluxo combinado pela equipe:

```bash
git pull origin main
```

### Enviar alterações

Depois de implementar e testar uma alteração:

```bash
git status
git add .
git commit -m "descreva a alteração realizada"
git push origin main
```

### Exemplos de mensagens de commit

```text
feat: implementa cadastro de produtos
feat: implementa entrada e saída
fix: impede saída acima do saldo
feat: adiciona relatórios de estoque
feat: adiciona histórico de movimentações
feat: implementa persistência JSON
feat: implementa menu principal
docs: atualiza documentação do projeto
test: registra testes do sistema
```

As mensagens devem representar as alterações realmente realizadas.

### Boas práticas de colaboração

- Trabalhar em alterações pequenas e coerentes.
- Revisar as diferenças antes de realizar o commit.
- Evitar alterações simultâneas no mesmo trecho sem alinhamento.
- Resolver conflitos com atenção.
- Testar o código integrado antes de considerar uma funcionalidade concluída.
- Manter o repositório atualizado.

## 11. Limitações e cuidados

O sistema foi desenvolvido para fins acadêmicos e possui as seguintes limitações:

- Os dados são armazenados localmente em arquivos JSON.
- Cópias diferentes do projeto não compartilham automaticamente os mesmos dados.
- Não há autenticação ou controle de acesso por usuário.
- Não há banco de dados servidor.
- A interface é exclusivamente de terminal.
- Não há sincronização automática entre computadores.
- O valor total representa uma estimativa baseada no preço unitário registrado e na quantidade disponível.
- Alterações manuais incorretas podem comprometer a estrutura dos arquivos JSON.
- O programa não possui recursos avançados de auditoria ou recuperação automática de dados.

Recomenda-se manter cópias de segurança dos arquivos JSON e evitar alterações manuais enquanto o programa estiver em execução.

Trata-se de um projeto acadêmico demonstrativo, não de um sistema comercial completo.

## 12. Integrantes

- Carlysson
- João Victor
- Paulo
- Paulista

Os nomes completos devem ser utilizados na versão final da documentação, conforme o padrão exigido pela instituição.

## 13. Licença

Este é um projeto acadêmico desenvolvido para fins educacionais.

Uma licença de software específica poderá ser adicionada pela equipe caso seja necessária para a publicação ou reutilização do código.

---

Desenvolvido em equipe como atividade acadêmica de programação imperativa.