# BiblioTech

Sistema de empréstimo de livros para a biblioteca do campus.

## 1. O projeto

O BiblioTech é um sistema para ajudar a biblioteca do campus a controlar os livros e os empréstimos. Ele resolve o problema de registrar empréstimos manualmente e permite que os leitores consultem a disponibilidade dos livros.

## 2. Histórias de usuário

| # | História de usuário |
|---|---|
| HU01 | Como leitor, quero consultar a disponibilidade de um livro, para saber se posso pegá-lo emprestado sem ir até o balcão. |
| HU02 | Como leitor, quero devolver um livro, para não ficar com pendência na biblioteca. |
| HU03 | Como bibliotecária, quero registrar um empréstimo, para saber quem está com cada exemplar. |
| HU04 | Como bibliotecária, quero cadastrar um livro novo, para que ele possa ser encontrado no sistema. |
| HU05 | Como bibliotecária, quero ver os empréstimos atrasados, para cobrar a devolução. |
| HU06 | Como leitor, quero reservar um livro, para conseguir pegá-lo quando estiver disponível. |

## 3. Requisitos

### Requisitos funcionais

| # | Requisito funcional | Veio da |
|---|---|---|
| RF01 | O sistema deve permitir que a bibliotecária cadastre um livro no acervo. | HU04 |
| RF02 | O sistema deve permitir que a bibliotecária cadastre um leitor. | Regra de acesso: só quem tem cadastro leva livro |
| RF03 | O sistema deve permitir que o leitor consulte a disponibilidade de um livro. | HU01 |
| RF04 | O sistema deve permitir que a bibliotecária registre a devolução de um livro. | HU02 |
| RF05 | O sistema deve permitir que a bibliotecária registre o empréstimo de um livro. | HU03 |
| RF06 | O sistema deve permitir que o leitor reserve um livro. | HU06 |

### Requisitos não funcionais

| # | Requisito não funcional |
|---|---|
| RNF01 | A consulta de disponibilidade deve responder em menos de 3 segundos. |
| RNF02 | Somente usuários identificados como bibliotecários podem alterar o acervo. |

## 4. Diagramas (feitos em APS)

### Casos de uso

![Diagrama de casos de uso do BiblioTech](docs/casos-de-uso.svg)

### Classes

![Diagrama de classes do BiblioTech](docs/classes.svg)

## 5. Decisão de modelagem: Bibliotecário e Empréstimo

Um bibliotecário pode registrar vários empréstimos, enquanto cada empréstimo é registrado por exatamente um bibliotecário.

A multiplicidade é **1 para 0..***: um bibliotecário pode registrar nenhum ou vários empréstimos, e cada empréstimo deve estar ligado a um único bibliotecário. Essa relação permite identificar qual bibliotecário realizou cada registro de empréstimo.

Na classe `Leitor`, o código acrescentou dois atributos ao modelo:

- `limiteEmprestimos`: quantidade máxima de livros que o leitor pode pegar emprestado.
- `livrosEmMaos`: quantidade de livros que o leitor está com ele no momento.

## 6. Classe Emprestimo

A classe `Emprestimo` representa o empréstimo de um livro para um leitor.

Ela mantém referências aos objetos `Livro` e `Leitor`, permitindo relacionar o livro emprestado à pessoa que o recebeu.

A classe também registra as datas de retirada e devolução e controla se o empréstimo está ativo.

As principais operações são:

- `realizarEmprestimo()`: verifica se o livro está disponível e se o leitor pode pegar outro livro antes de registrar o empréstimo.
- `registrarDevolucao()`: registra a devolução e atualiza a disponibilidade do livro e a quantidade de livros com o leitor.
- `estaAtivo()`: informa se o empréstimo continua ativo.

O método `realizarEmprestimo()` impede empréstimos inválidos sem alterar os dados do livro ou do leitor. Já `registrarDevolucao()` verifica se o empréstimo está ativo, evitando que uma segunda devolução altere os dados novamente.

A classe `TesteEmprestimo` verifica essas situações, incluindo empréstimo realizado, livro indisponível, limite de empréstimos e devolução.

**Observação:** neste estágio, o empréstimo relaciona diretamente um livro e um leitor. O registro do bibliotecário responsável, descrito na seção 5, ainda não foi implementado na classe `Emprestimo`.