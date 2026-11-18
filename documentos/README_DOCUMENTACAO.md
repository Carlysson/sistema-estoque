# Orientações para a documentação em PDF

Este diretório será utilizado para armazenar o documento PDF final do projeto. **O PDF não faz parte da versão-base:** a equipe deverá elaborá-lo após implementar e testar as funcionalidades.

## 1. Objetivo do documento

O PDF deverá apresentar o problema abordado, o objetivo do sistema, as funcionalidades que foram realmente implementadas, a aplicação do paradigma imperativo e evidências que comprovem a execução e os testes.

O texto deve corresponder à versão do código entregue. Não descreva como concluída uma funcionalidade que ainda esteja pendente.

## 2. Estrutura sugerida

Organizem o documento nesta sequência:

1. Capa.
2. Problema, objetivo e solução proposta.
3. Funcionalidades implementadas.
4. Paradigma imperativo e conceitos identificados no código.
5. Evidências de execução e testes.
6. Considerações finais.

A estrutura poderá ser adaptada às exigências específicas do professor ou da instituição.

## 3. Informações da capa

Incluam, conforme o padrão institucional:

- Nome da instituição.
- Curso e disciplina.
- Nome do professor.
- Título: **Sistema de Gerenciamento de Estoque**.
- Nome completo dos quatro integrantes: Carlysson, João Victor, Paulo e Paulista.
- Cidade e ano/semestre, se exigidos.

Confirmem a grafia e a forma completa dos nomes antes da entrega.

## 4. Problema e solução

Contextualizem as dificuldades do controle manual de mercadorias, como divergências de quantidade, demora para localizar produtos e dificuldade de identificar itens em falta.

Em seguida, apresentem a proposta de um sistema de terminal desenvolvido em Python 3, com organização procedural e armazenamento local em JSON. Diferenciem claramente os objetivos planejados daquilo que foi efetivamente construído.

## 5. Funcionalidades implementadas

Descrevam as funcionalidades que estiverem concluídas na versão final, por exemplo:

- Cadastro, listagem e localização de produtos.
- Registro de entradas e saídas.
- Atualização e validação dos saldos.
- Relatórios de estoque mínimo, valor total e produtos disponíveis.
- Consulta do histórico.
- Persistência dos dados em JSON.

Para cada item, expliquem brevemente seu comportamento e indiquem eventuais limitações. Removam da descrição qualquer funcionalidade que não tenha sido implementada ou testada.

## 6. Paradigma imperativo

Expliquem que o paradigma imperativo organiza a solução em instruções executadas em sequência, com variáveis, atribuições, decisões, repetições e funções.

Demonstrem **pelo menos três conceitos** com exemplos reais retirados do código final. Para cada conceito:

1. Identifiquem o conceito.
2. Expliquem seu significado.
3. Apresentem um pequeno trecho de código ou indiquem a função em que aparece.
4. Relacionem o trecho a uma operação do sistema.

Podem ser utilizados variáveis e atribuições, condicionais (`if`, `elif`, `else`), repetições (`while`, `for`), funções/procedimentos e sequência de comandos. Os exemplos devem ser do código desenvolvido pela equipe, não trechos hipotéticos apresentados como se estivessem prontos.

## 7. Inserção das evidências

Insiram capturas reais da execução do programa, com legenda e breve explicação. As imagens devem demonstrar os resultados dos testes descritos no relatório.

Verifiquem se os textos estão legíveis e se os dados exibidos correspondem à versão final. Não usem imagens montadas ou capturas de funcionalidades que não existem.

A pasta `evidencias/` possui um arquivo de orientação com a lista de capturas recomendadas.

## 8. Considerações finais

Registrem o que foi alcançado, como a equipe dividiu e integrou o trabalho, quais dificuldades técnicas surgiram e como foram resolvidas. Mencionem limitações que permaneceram e possíveis melhorias, sem afirmar que foram implementadas.

## 9. Formatação e revisão

- Sigam o modelo e as regras de formatação fornecidos pela instituição.
- Utilizem títulos e subtítulos consistentes.
- Mantenham linguagem clara, objetiva e técnica.
- Identifiquem tabelas, figuras e capturas.
- Revisem ortografia, nomes, numeração de páginas e referências, se houver.
- Confiram se todas as imagens estão legíveis no PDF exportado.
- Verifiquem se o documento descreve exatamente a versão do código que será entregue.

**Importante:** este arquivo é apenas um roteiro. A equipe deverá produzir o PDF final e salvá-lo neste diretório.
