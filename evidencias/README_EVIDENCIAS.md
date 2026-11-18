# Orientações para as evidências de execução

Esta pasta será utilizada para armazenar capturas de tela que comprovem a execução e os testes do Sistema de Gerenciamento de Estoque.

**Não existem evidências nesta versão-base**, pois as funcionalidades ainda serão desenvolvidas. As capturas deverão ser produzidas pela equipe depois que cada operação estiver implementada e testada.

## 1. Capturas necessárias

Organizem as evidências para demonstrar, quando disponíveis:

1. **Menu principal:** apresentação das opções do sistema.
2. **Cadastro de produtos:** preenchimento dos dados e confirmação do cadastro.
3. **Listagem de produtos:** produtos cadastrados apresentados no terminal.
4. **Entrada de mercadorias:** operação concluída e saldo atualizado.
5. **Saída de mercadorias:** operação concluída e saldo atualizado.
6. **Bloqueio de saída acima do saldo:** tentativa de retirar quantidade maior que a disponível e mensagem de bloqueio.
7. **Relatório de estoque baixo:** produtos abaixo do estoque mínimo.
8. **Relatório de valor total:** cálculo estimado do valor armazenado.
9. **Relatório de produtos disponíveis:** produtos com quantidade maior que zero.
10. **Histórico de movimentações:** registros com tipo, produto, quantidade, data/hora e saldos anterior e atual.

## 2. Como organizar

- Salvem as imagens nesta pasta `evidencias/`.
- Utilizem nomes claros e numerados, por exemplo:
  - `01-menu-principal.png`
  - `02-cadastro-produto.png`
  - `03-listagem-produtos.png`
  - `04-entrada-mercadoria.png`
  - `05-saida-mercadoria.png`
  - `06-bloqueio-saida-excessiva.png`
  - `07-relatorio-estoque-baixo.png`
  - `08-relatorio-valor-total.png`
  - `09-produtos-disponiveis.png`
  - `10-historico-movimentacoes.png`
- Mantenham resolução suficiente para leitura dos textos.
- Se uma operação exigir mais de uma tela, utilizem capturas complementares e expliquem a sequência no PDF.

## 3. Critérios de validade

As capturas devem:

- Ser legíveis e mostrar o resultado relevante.
- Apresentar resultados reais obtidos pela execução do programa.
- Corresponder à versão final do código entregue.
- Ser produzidas pela própria equipe durante os testes.
- Não ser montadas para simular funcionalidades.
- Não ocultar mensagens de erro relevantes nem apresentar resultados que não possam ser reproduzidos.

Utilizem dados de teste cadastrados pela equipe. Os arquivos JSON da versão-base começam vazios; não há produtos ou movimentações fictícias fornecidas.

## 4. Relação com o PDF

Incluam no PDF as capturas mais relevantes, com número, legenda e explicação breve do cenário testado. Confiram se cada evidência está associada a uma funcionalidade realmente implementada e se o resultado apresentado é coerente com o código.

Este diretório contém apenas as orientações iniciais. A equipe deverá adicionar as imagens reais após a implementação.
