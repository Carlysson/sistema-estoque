# Sistema de Gerenciamento de Estoque

Projeto acadêmico desenvolvido em **Python 3**, com interface de terminal e armazenamento local em arquivos JSON. A proposta é apoiar o controle de mercadorias de pequenos comércios e, principalmente, aplicar os conceitos de **programação imperativa** por meio de uma organização procedural baseada em funções.

> **ATENÇÃO — VERSÃO-BASE PARA DESENVOLVIMENTO COLABORATIVO**
>
> As funcionalidades descritas neste documento são requisitos planejados e **ainda precisam ser implementadas pela equipe**. Esta entrega contém a estrutura inicial, os pontos de partida do código e as orientações de trabalho. Não é um sistema comercial, multiusuário ou concluído.

## 1. Objetivo e problema

O controle manual de mercadorias pode provocar divergências entre a quantidade anotada e a quantidade realmente disponível. Também pode dificultar a identificação de produtos em falta, atrasar consultas e tornar trabalhoso estimar o valor armazenado no comércio.

A proposta é reunir essas operações em um programa simples executado pelo terminal. Quando desenvolvido, o sistema deverá permitir que a equipe registre produtos, acompanhe entradas e saídas, consulte relatórios e mantenha os dados salvos localmente.

Além de propor uma solução para esse problema, o objetivo acadêmico é aplicar a programação imperativa em Python: organizar instruções em sequência, utilizar variáveis, decisões, repetições e funções para modificar e consultar os dados.

## 2. Funcionalidades a implementar

As funcionalidades abaixo representam os requisitos do sistema final. As marcadas com ✅ já foram implementadas; as demais ainda estão em desenvolvimento.

1. **Cadastro de produtos:** registrar código, nome, preço, quantidade inicial e estoque mínimo.
2. **Listagem de produtos:** apresentar os produtos cadastrados e suas informações.
3. **Entrada de mercadorias:** registrar o recebimento de determinada quantidade de um produto.
4. **Saída de mercadorias:** registrar a retirada de determinada quantidade.
5. **Atualização do estoque:** atualizar a quantidade disponível após cada entrada ou saída.
6. **Validação de saída:** bloquear uma retirada cuja quantidade seja maior que o saldo disponível.
7. ✅ **Relatório de estoque baixo:** identificar produtos cuja quantidade esteja abaixo do estoque mínimo definido.
8. ✅ **Cálculo do valor total:** estimar o valor armazenado usando preço unitário × quantidade disponível.
9. ✅ **Relatório de produtos disponíveis:** apresentar produtos com quantidade maior que zero.
10. ✅ **Histórico de movimentações:** consultar data/hora, tipo de operação, produto, quantidade e saldos anterior e atual.
11. **Persistência em JSON:** salvar e recuperar os cadastros e as movimentações em arquivos locais.

A equipe deverá implementar, testar e integrar essas operações. A presença de uma função planejada em `estoque.py` não significa que sua funcionalidade esteja pronta.

## 3. Requisitos e ferramentas

| Item | Requisito |
|---|---|
| Linguagem | Python 3 |
| Versão recomendada | Python 3.10 ou superior |
| Interface | Terminal/console |
| Armazenamento previsto | Arquivos JSON locais |
| Paradigma | Programação imperativa |
| Organização | Programação procedural por funções |
| Versionamento | Git e GitHub |
| Bibliotecas externas | Nenhuma necessária para a proposta inicial |

Será possível utilizar o Prompt de Comando, PowerShell, terminal do Linux/macOS ou terminal integrado de uma IDE. O projeto não exige banco de dados ou interface gráfica.

## 4. Como executar a versão-base

1. Baixe o ZIP do projeto ou clone o repositório GitHub.
2. Se tiver baixado o ZIP, extraia a pasta.
3. Abra o terminal dentro da pasta `sistema-estoque/`, onde está localizado o arquivo `main.py`.
4. Execute:

```bash
python main.py
```

Dependendo da instalação do Python, também poderá ser necessário utilizar:

```bash
python3 main.py
```

ou, no Windows:

```bash
py main.py
```

Nesta etapa, a execução deverá apenas exibir uma mensagem informando que o projeto está em desenvolvimento. **Ainda não existe um menu funcional e não será possível cadastrar ou movimentar produtos.** Isso é intencional: as funcionalidades serão desenvolvidas pelos integrantes.

Após a implementação do sistema, o menu deverá oferecer uma opção `0` para encerrar o programa. A equipe deverá combinar o comportamento do menu e sua integração com as demais funções.

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
│   └── README_DOCUMENTACAO.md
│
└── evidencias/
    └── README_EVIDENCIAS.md
```

### Finalidade dos arquivos e diretórios

| Caminho | Finalidade |
|---|---|
| `main.py` | Ponto de entrada. Importa `executar()` de `estoque.py` e chama essa função quando o arquivo é executado diretamente. Não deve concentrar funcionalidades de estoque. |
| `estoque.py` | Arquivo central das funções do sistema. Contém, nesta versão, apenas os pontos de partida, docstrings e marcações `TODO`. |
| `README.md` | Documentação principal: objetivo, requisitos, arquitetura, responsabilidades, testes e orientações de colaboração. |
| `.gitignore` | Evita versionar arquivos temporários, ambientes virtuais e configurações locais desnecessárias. |
| `dados/produtos.json` | Arquivo reservado aos dados dos produtos. Começa vazio (`[]`). |
| `dados/movimentacoes.json` | Arquivo reservado ao histórico de entradas e saídas. Começa vazio (`[]`). |
| `dados/.gitkeep` | Arquivo vazio para manter a pasta `dados/` no controle de versão mesmo quando estiver sem outros arquivos. |
| `documentos/` | Local destinado ao documento PDF final. O README interno explica como prepará-lo. |
| `evidencias/` | Local destinado às capturas de tela reais da execução e dos testes. |

Os dois arquivos JSON começam vazios. A equipe deverá desenvolver as rotinas de leitura e gravação e definir, em conjunto, a estrutura dos registros. Não há produtos fictícios ou movimentações de demonstração. Evitem editar os JSON manualmente enquanto o programa estiver em execução e mantenham cópias de segurança durante o desenvolvimento.

## 6. Paradigma imperativo: conceitos no código

O **paradigma imperativo** descreve a solução por meio de instruções que determinam, passo a passo, o que o programa deve executar. Essas instruções podem consultar valores, tomar decisões, repetir operações e alterar o estado dos dados.

O projeto deverá utilizar programação **procedural por funções**. Não é necessário criar classes próprias como estrutura central da aplicação. Os dados poderão ser representados por estruturas simples do Python, como listas e dicionários, conforme o formato que a equipe combinar.

A seguir estão cinco conceitos que deverão ser identificados e demonstrados no código final. Os exemplos indicam onde poderão aparecer; não representam funcionalidades já implementadas.

### 6.1 Variáveis e atribuições

Variáveis armazenam valores que serão utilizados durante a execução. A atribuição associa um valor a um nome e o programa poderá atualizar esse valor conforme as operações realizadas.

No sistema, poderão ser utilizadas para guardar o código de um produto, seu preço, a quantidade solicitada e o saldo atual. Por exemplo, durante uma entrada, uma variável de saldo poderá receber o valor anterior somado à quantidade recebida.

Isso caracteriza a programação imperativa porque o programa executa comandos que consultam e modificam valores ao longo do procedimento.

### 6.2 Condicionais (`if`, `elif`, `else`)

As condicionais permitem escolher qual conjunto de instruções será executado conforme uma condição.

No sistema, deverão aparecer, por exemplo, na validação de um código, na verificação de campos obrigatórios e na regra que impede uma saída maior que o saldo disponível. A equipe poderá utilizar `if`, `elif` e `else` para tratar os diferentes resultados.

Esse conceito é imperativo porque determina explicitamente o caminho de execução que o programa seguirá.

### 6.3 Estruturas de repetição (`while`, `for`)

As estruturas de repetição executam instruções mais de uma vez. O `while` repete enquanto uma condição for verdadeira; o `for` percorre os elementos de uma sequência.

No sistema final, um `while` poderá manter o menu ativo até que o usuário escolha encerrar. Um `for` poderá percorrer a lista de produtos para exibi-los ou verificar quais estão abaixo do estoque mínimo.

A repetição caracteriza a programação imperativa porque descreve explicitamente a execução sucessiva de comandos.

### 6.4 Funções e procedimentos

Funções agrupam instruções relacionadas a uma tarefa e permitem organizar o programa em partes menores. Podem receber parâmetros e, quando necessário, retornar resultados.

No projeto, funções como `cadastrar_produto()`, `registrar_entrada()` e `exibir_historico()` deverão concentrar responsabilidades específicas. As assinaturas iniciais estão em `estoque.py`, mas seus corpos ainda precisam ser desenvolvidos.

A organização em funções não transforma automaticamente o programa em orientado a objetos. O projeto continuará procedural se a equipe utilizar funções e estruturas de dados simples, sem adotar classes próprias como estrutura central.

### 6.5 Sequência de comandos

A sequência representa a ordem em que as instruções são executadas. A ordem é importante porque algumas etapas dependem dos resultados das anteriores.

Em uma futura saída de mercadoria, por exemplo, o programa deverá localizar o produto, receber a quantidade solicitada, verificar o saldo, atualizar a quantidade e registrar a movimentação. A equipe deverá implementar e testar essa ordem.

Esse conceito caracteriza a programação imperativa porque a solução é descrita como uma sequência explícita de ações.

## 7. Divisão de responsabilidades

A divisão abaixo foi combinada pela equipe e deverá ser preservada durante o desenvolvimento.

| Integrante | Responsabilidade principal | Atividades |
|---|---|---|
| **Carlysson** | Coordenação e integração | Organizar o repositório, integrar e revisar as alterações, acompanhar o menu e o fluxo principal, consolidar a documentação e coordenar a entrega. |
| **João Victor** | Relatórios e históricos | Implementar e revisar o relatório de estoque mínimo, o cálculo do valor total e o relatório de produtos disponíveis; exibir o histórico; conferir os resultados com os dados registrados. |
| **Paulo** | Entradas e saídas | Registrar entradas e saídas, atualizar quantidades, impedir retiradas acima do saldo e gravar os dados de cada movimentação. |
| **Paulista** | Cadastro e listagem | Implementar cadastro, listagem, localização de produtos e validações cadastrais, como código duplicado e campos inválidos. |

### Combinados de equipe

- Cada integrante deverá trabalhar principalmente na tarefa que lhe foi atribuída.
- Mudanças que afetem outras partes do sistema deverão ser comunicadas aos demais integrantes.
- Evitem editar simultaneamente o mesmo trecho de `estoque.py` sem alinhamento prévio.
- Façam commits pequenos, frequentes e verdadeiros, descrevendo as alterações realizadas.
- Testem a parte desenvolvida antes de integrá-la à versão compartilhada.
- Todos deverão conhecer o funcionamento geral e conseguir explicar o projeto.
- Carlysson coordenará a integração e acompanhará o fluxo principal.
- **Paulo registra as movimentações** de entrada e saída; **João Victor consulta e apresenta o histórico** dessas movimentações. São responsabilidades diferentes e complementares.

### Sequência sugerida de desenvolvimento

1. Ler os requisitos, conferir a estrutura e executar a versão-base.
2. Implementar e testar cadastro, listagem, localização e validações cadastrais.
3. Implementar e testar entradas, saídas, atualização do saldo e bloqueio de saída excessiva.
4. Implementar e testar relatórios e consulta do histórico.
5. Integrar as alterações e resolver conflitos.
6. Testar o fluxo completo com dados cadastrados pela própria equipe.
7. Preparar o PDF, as evidências e a apresentação.

### Integração em `estoque.py`

Todos trabalharão principalmente no mesmo arquivo, `estoque.py`. Por isso, antes de implementar, combinem os nomes das funções, seus parâmetros, os valores que retornam e a forma como os dados serão compartilhados. Por exemplo, as funções de relatório precisarão consultar a mesma estrutura de produtos que as funções de cadastro e movimentação atualizam.

Não alterem a assinatura de uma função utilizada por outro integrante sem avisar e combinar a mudança. Se houver conflito no Git, conversem e revisem o resultado antes de concluir a integração.

### 7.1 Contrato de dados e funções

**Todos devem seguir exatamente estes nomes e tipos.** Qualquer mudança deve ser combinada no grupo antes.

#### Arquivos

| Arquivo | Conteúdo |
|---|---|
| `dados/produtos.json` | Lista de produtos (`[]` quando vazio) |
| `dados/movimentacoes.json` | Lista de movimentações, da mais antiga para a mais recente (`[]` quando vazio) |

No topo do `estoque.py`, usar constantes para os caminhos:

```python
ARQUIVO_PRODUTOS = "dados/produtos.json"
ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.json"
```

#### Produto (cada item de `produtos.json`)

```json
{"codigo": "001", "nome": "Arroz 5kg", "preco": 25.90, "quantidade": 10, "estoque_minimo": 5}
```

| Campo | Tipo | Regra |
|---|---|---|
| `codigo` | `str` | Único e não vazio. É texto para manter zeros à esquerda (`"001"`). |
| `nome` | `str` | Não vazio. |
| `preco` | `float` | Maior que 0. |
| `quantidade` | `int` | Maior ou igual a 0. É o saldo atual. |
| `estoque_minimo` | `int` | Maior ou igual a 0. |

#### Movimentação (cada item de `movimentacoes.json`)

```json
{"data_hora": "18/11/2026 21:30:05", "tipo": "entrada", "codigo": "001",
 "nome": "Arroz 5kg", "quantidade": 5, "saldo_anterior": 10, "saldo_atual": 15}
```

| Campo | Tipo | Regra |
|---|---|---|
| `data_hora` | `str` | Formato `"%d/%m/%Y %H:%M:%S"`, gerado com `datetime.now()`. |
| `tipo` | `str` | Exatamente `"entrada"` ou `"saida"` (minúsculo, sem acento). |
| `codigo`, `nome` | `str` | Copiados do produto no momento da operação. |
| `quantidade` | `int` | Maior que 0. Quantidade movimentada. |
| `saldo_anterior`, `saldo_atual` | `int` | Saldo antes e depois da operação. |

#### Funções compartilhadas

| Função | Responsável | Contrato |
|---|---|---|
| `carregar_dados(caminho)` | Carlysson | Retorna uma `list`. Se o arquivo não existir, estiver vazio ou inválido, retorna `[]` (sem quebrar o programa). |
| `salvar_dados(caminho, dados)` | Carlysson | Grava a lista em JSON (`indent=4`, `ensure_ascii=False`). |
| `localizar_produto(codigo)` | Paulista | Retorna o `dict` do produto ou `None` se não existir. |
| `registrar_movimentacao(produto, tipo, quantidade, saldo_anterior, saldo_atual)` | Paulo | Monta o dicionário da movimentação (tabela acima) e o grava em `movimentacoes.json`. |

#### Regras gerais

- Quem **altera** produtos (cadastro, entrada e saída) deve chamar `salvar_dados(ARQUIVO_PRODUTOS, produtos)` logo após a alteração.
- As funções de relatório e histórico (`relatorio_estoque_baixo`, `calcular_valor_total`, `listar_produtos_disponiveis`, `exibir_historico`) **não recebem parâmetros**, apenas leem os arquivos com `carregar_dados` e **não modificam** os dados.
- "Abaixo do mínimo" significa `quantidade < estoque_minimo`. "Disponível" significa `quantidade > 0`.
- Valores em reais são exibidos com 2 casas decimais, por exemplo `R$ 25.90`.
- Funções de entrada de dados (`input`) devem tratar valores inválidos e repetir a pergunta, sem fechar o programa.

## 8. Roteiro de testes

A tabela apresenta cenários que deverão ser testados quando as funcionalidades correspondentes estiverem implementadas. Os dados necessários deverão ser cadastrados pela equipe, pois os arquivos JSON começam vazios.

| Cenário | Ação | Resultado esperado |
|---|---|---|
| Cadastro correto | Inserir código novo e dados válidos. | Produto salvo e listado. |
| Código duplicado | Repetir um código existente. | Cadastro recusado. |
| Campo vazio | Não informar campo obrigatório. | Solicitação de novo valor ou mensagem de validação. |
| Preço inválido | Informar texto, zero ou valor negativo. | Solicitação de preço válido. |
| Entrada | Dar entrada em produto existente. | Saldo aumenta e evento entra no histórico. |
| Saída válida | Retirar quantidade disponível. | Saldo diminui e evento entra no histórico. |
| Saída excessiva | Retirar mais do que o saldo. | Operação bloqueada e saldo preservado. |
| Código inexistente | Movimentar produto não cadastrado. | Mensagem de produto não encontrado. |
| Estoque mínimo | Consultar relatório com item abaixo do mínimo. | Item aparece no relatório. |
| Valor total | Consultar valor armazenado. | Soma de preço × quantidade de todos os produtos. |
| Persistência | Fechar e abrir novamente. | Cadastro e histórico continuam gravados. |

Registrem os resultados dos testes e corrijam os problemas encontrados antes de integrar. Não utilizem registros fictícios como se fossem evidências de execução real.

## 9. Evidências e documento PDF

As capturas de tela deverão ser salvas em `evidencias/`. Quando as funcionalidades estiverem prontas, a equipe deverá produzir evidências legíveis de:

- Menu principal.
- Cadastro e listagem de produtos.
- Entrada e saída de mercadorias.
- Tentativa de saída acima do saldo e respectivo bloqueio.
- Relatório de produtos abaixo do estoque mínimo.
- Relatório de valor total armazenado.
- Histórico de movimentações.

O arquivo `evidencias/README_EVIDENCIAS.md` contém uma lista mais detalhada e orientações para nomear e organizar as capturas.

### Estrutura recomendada para o PDF

1. **Capa:** instituição, disciplina, professor e nomes dos integrantes.
2. **Problema, objetivo e solução proposta:** contextualização do controle de estoque e apresentação da proposta.
3. **Funcionalidades implementadas:** descrição somente do que estiver realmente pronto na versão entregue.
4. **Paradigma imperativo:** explicação de pelo menos três conceitos demonstrados com exemplos reais do código.
5. **Evidências dos testes e da execução:** capturas que comprovem o funcionamento.
6. **Considerações finais:** resultados alcançados, dificuldades e possíveis melhorias.

O documento `documentos/README_DOCUMENTACAO.md` apresenta orientações para elaborar e revisar o PDF. As evidências devem corresponder à versão real do programa. **Não incluam capturas de menus ou funcionalidades que ainda não existam.**

## 10. Git e GitHub

O repositório remoto deverá se chamar:

`sistema-estoque`

Descrição sugerida:

`Sistema de gerenciamento de estoque em Python utilizando programação imperativa.`

### Configuração inicial

Com o Git instalado, abra o terminal na pasta raiz do projeto e execute:

```bash
git init
git add .
git commit -m "chore: cria estrutura inicial do projeto"
git branch -M main
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

Substitua `URL_DO_REPOSITORIO` pela URL real do repositório criado no GitHub. Não digite esse texto literalmente como endereço remoto.

### Enviar alterações posteriores

Depois de implementar e testar uma alteração:

```bash
git add .
git commit -m "feat: descreve a funcionalidade implementada"
git push
```

### Exemplos de mensagens de commit

- `docs: detalha instruções e divisão de tarefas`
- `feat: implementa cadastro de produtos`
- `feat: implementa entrada e saída`
- `fix: impede saída acima do saldo`
- `feat: adiciona relatórios de estoque`
- `feat: adiciona histórico de movimentações`
- `test: verifica validações e relatórios`
- `docs: adiciona PDF e evidências`

As mensagens devem descrever o que realmente mudou. Não criem commits artificiais para aparentar participação: o histórico do Git deve representar a evolução verdadeira do trabalho de cada integrante.

### Boas práticas de colaboração

- Antes de começar uma tarefa, atualize sua cópia local conforme o fluxo combinado pela equipe.
- Evite que duas pessoas alterem simultaneamente o mesmo trecho.
- Faça commits pequenos e relacionados a uma alteração coerente.
- Leia as diferenças antes de confirmar um commit.
- Revise conflitos com atenção; não aceite alterações sem compreender o que será mantido.
- Teste a versão integrada antes de considerar uma tarefa concluída.

## 11. Limitações e cuidados

A proposta utiliza arquivos JSON locais e possui limitações importantes:

- Os dados ficam armazenados localmente em arquivos JSON.
- Cópias diferentes do projeto não compartilham automaticamente os mesmos dados.
- Não há autenticação nem controle de acesso por usuário.
- Não há banco de dados servidor.
- Não há interface gráfica; a interação será feita pelo terminal.
- Não há sincronização automática entre computadores.
- O valor total será uma estimativa baseada no preço unitário registrado e no saldo atual; não representa necessariamente o valor contábil ou comercial completo do negócio.
- Trata-se de um projeto acadêmico e demonstrativo, não de um sistema comercial pronto.
- Alterações manuais incorretas podem invalidar a estrutura dos JSON. Mantenham cópias de segurança e evitem editar os arquivos enquanto o programa estiver rodando.

## 12. Integrantes

- Carlysson
- João Victor
- Paulo
- Paulista

Antes da entrega, adicionem os nomes completos conforme o padrão exigido pela instituição e confiram a identificação de todos os integrantes na capa do PDF e no repositório, se necessário.

## 13. Licença

Este é um projeto acadêmico desenvolvido para fins educacionais. Uma licença de software específica poderá ser adicionada pelo grupo caso seja necessária para a publicação ou reutilização do código.

---

Desenvolvido em equipe como atividade acadêmica de programação imperativa.
