# BiblioTech

Sistema de emprestimo de livros para a biblioteca do campus.

## 1. O projeto

O BiblioTech é um sistema para ajudar a biblioteca do campus a controlar os livros e os emprestimos. Ele resolve o problema de registrar emprestimos manualmente e permite que os leitores consultem a disponibilidade dos livros.

## 2. Historias de usuario

| # | Historia de usuario |
|---|---|
| HU01 | Como leitor, quero consultar a disponibilidade de um livro, para saber se posso pega-lo emprestado sem ir ate o balcao. |
| HU02 | Como leitor, quero devolver um livro, para nao ficar com pendencia na biblioteca. |
| HU03 | Como bibliotecaria, quero registrar um emprestimo, para saber quem esta com cada exemplar. |
| HU04 | Como bibliotecaria, quero cadastrar um livro novo, para que ele possa ser encontrado no sistema. |
| HU05 | Como bibliotecaria, quero ver os emprestimos atrasados, para cobrar a devolucao. |
| HU06 | Como leitor, quero reservar um livro, para conseguir pega-lo quando estiver disponivel. |

## 3. Requisitos

### Requisitos funcionais

| # | Requisito funcional | Veio da |
|---|---|---|
| RF01 | O sistema deve permitir que a bibliotecaria cadastre um livro no acervo. | HU04 |
| RF02 | O sistema deve permitir que a bibliotecaria cadastre um leitor. | regra de acesso: so quem tem cadastro leva livro |
| RF03 | O sistema deve permitir que o leitor consulte a disponibilidade de um livro. | HU01 |
| RF04 | O sistema deve permitir que a bibliotecaria registre a devolucao de um livro. | HU02 |
| RF05 | O sistema deve permitir que a bibliotecaria registre o emprestimo de um livro. | HU03 |
| RF06 | O sistema deve permitir que o leitor reserve um livro. | HU06 |

### Requisitos nao funcionais

| # | Requisito nao funcional |
|---|---|
| RNF01 | A consulta de disponibilidade deve responder em menos de 3 segundos. |
| RNF02 | Somente usuarios identificados como bibliotecarios podem alterar o acervo. |

## 4. Diagramas (feitos em APS)

### Casos de uso

![Diagrama de casos de uso do BiblioTech](docs/casos-de-uso.svg)

### Classes

![Diagrama de classes do BiblioTech](docs/classes.svg)

## 5. Decisão de modelagem: Bibliotecario e Emprestimo

Um bibliotecario pode registrar varios emprestimos, enquanto cada emprestimo e registrado por exatamente um bibliotecario.

A multiplicidade e **1 para 0..***: um bibliotecario pode registrar nenhum ou varios emprestimos, e cada emprestimo deve estar ligado a um unico bibliotecario. Essa relacao permite identificar qual bibliotecario realizou cada registro de emprestimo.

Na classe `Leitor`, o codigo acrescentou dois atributos ao modelo:

- `limiteEmprestimos`: quantidade maxima de livros que o leitor pode pegar emprestado.
- `livrosEmMaos`: quantidade de livros que o leitor esta com ele no momento.