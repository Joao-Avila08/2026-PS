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

A multiplicidade é **1 para 0..\***: um bibliotecário pode registrar nenhum ou vários empréstimos, e cada empréstimo deve estar ligado a um único bibliotecário. Essa relação permite identificar qual bibliotecário realizou cada registro de empréstimo.

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

## 7. Classe Biblioteca — Aula 39

A classe `Biblioteca` reúne os elementos necessários para controlar o funcionamento do sistema, organizando o acervo, os leitores cadastrados e os empréstimos realizados.

Ela funciona como intermediária entre as solicitações feitas pelo usuário e as operações executadas pelas classes `Livro`, `Leitor` e `Emprestimo`.

Entre suas principais responsabilidades estão:

- Consultar o acervo e localizar livros.
- Localizar leitores por meio de suas matrículas.
- Verificar se um livro pode ser emprestado.
- Solicitar a realização de empréstimos.
- Registrar devoluções e impedir devoluções repetidas.
- Fornecer informações sobre os livros e os empréstimos registrados.

O método `emprestar()` recebe o título de um livro e a matrícula de um leitor. A partir dessas informações, a biblioteca verifica os dados necessários e solicita a operação de empréstimo, respeitando as regras de disponibilidade e o limite de livros do leitor.

O método `devolver()` solicita a devolução de um livro, considerando se existe um empréstimo ativo correspondente. Dessa forma, uma segunda devolução do mesmo empréstimo é recusada.

O método `obterAcervoComoTexto()` fornece uma representação textual do acervo, incluindo as informações dos livros e seus estados de disponibilidade. Esse método permite que outras partes do sistema apresentem o acervo sem precisar reproduzir toda a lógica de consulta.

A classe `TesteBiblioteca` verifica o funcionamento integrado do sistema, incluindo a localização de livros e leitores, a realização de empréstimos, o controle do limite do leitor, a recusa de operações inválidas e o registro de devoluções.

## 8. Interface gráfica — Aula 40

A classe `TelaBiblioteca` implementa a primeira interface gráfica do BiblioTech. Ela permite que o usuário interaja com as operações da biblioteca por meio de campos de texto, botões e uma área de exibição do acervo.

### 8.1. Integração com a classe Biblioteca

A janela mantém um objeto da classe `Biblioteca` no atributo `biblioteca`. Os botões utilizam esse mesmo objeto para consultar o acervo, realizar empréstimos e registrar devoluções.

Essa organização permite que a interface encaminhe as solicitações à classe responsável pelas operações, sem precisar implementar novamente as regras de empréstimo e devolução.

### 8.2. Campos e botões

A interface possui os seguintes elementos:

- `campoTitulo`: campo utilizado para informar o título do livro.
- `campoMatricula`: campo utilizado para informar a matrícula do leitor.
- `areaAcervo`: área destinada à exibição das informações dos livros.
- `botaoEmprestar`: solicita a realização de um empréstimo.
- `botaoDevolver`: solicita a devolução de um livro.
- `botaoAtualizar`: atualiza as informações exibidas no acervo.

A área de exibição do acervo é destinada à consulta das informações, evitando que o usuário altere diretamente o texto apresentado.

### 8.3. Funcionamento dos botões

Os botões são conectados às operações por meio de `addActionListener`, que permite executar um método quando o usuário clica em um botão.

O botão Emprestar chama o método `emprestar()`. Esse método obtém o título e a matrícula informados, verifica se os campos obrigatórios foram preenchidos e solicita a operação por meio de `biblioteca.emprestar(titulo, matricula)`.

Após a tentativa, a interface atualiza as informações do acervo e apresenta uma mensagem indicando o resultado da operação.

O botão Devolver chama o método `devolver()`, que obtém o título informado, verifica se o campo foi preenchido e solicita a devolução por meio da biblioteca. A interface apresenta uma mensagem correspondente ao resultado.

O botão Atualizar chama `atualizarAcervo()`, permitindo consultar novamente as informações dos livros.

### 8.4. Atualização do acervo

O método `atualizarAcervo()` utiliza `biblioteca.obterAcervoComoTexto()` para obter as informações atualizadas e exibi-las na área de texto da janela.

Essa atualização permite visualizar as mudanças de disponibilidade após empréstimos e devoluções. Sem ela, a interface poderia continuar apresentando informações anteriores à operação realizada.

### 8.5. Tratamento de operações inválidas

A interface verifica se os campos obrigatórios estão vazios e orienta o usuário a preenchê-los. Além disso, apresenta mensagens de sucesso ou falha para informar o resultado das operações.

As regras de negócio continuam sendo responsabilidade da biblioteca e das classes relacionadas. Assim, a interface não deve permitir que um livro já emprestado seja emprestado novamente nem que um leitor ultrapasse seu limite de empréstimos.

## 9. Testes e verificação do funcionamento

Os testes das classes anteriores continuam fazendo parte do projeto. A classe `TesteBiblioteca` verifica as operações da biblioteca, incluindo empréstimos aceitos e recusados, controle de limites e devoluções.

Na Aula 40, o projeto também passou pela compilação com `javac *.java`, sem apresentar mensagens de erro. A execução de `java TesteBiblioteca` apresentou os resultados esperados para os cenários testados, incluindo a recusa de um segundo empréstimo do mesmo livro enquanto ele está emprestado e a recusa de uma segunda devolução.

O código da interface foi conectado aos métodos responsáveis pelas operações da biblioteca. Entretanto, a verificação visual da janela ainda depende da resolução do problema de inicialização do ambiente gráfico.

O projeto possui commits e push registrados no GitHub para as alterações de preparação do ambiente e integração da janela com o acervo e as operações de empréstimo.

## 10. Como executar

Para compilar e executar os testes, abra o terminal na pasta `bibliotech` e execute:

```bash
javac *.java
java TesteBiblioteca
java TesteRequisitos
```

A compilação deve terminar sem erros. A classe `TesteBiblioteca` demonstra as operações principais do sistema, enquanto `TesteRequisitos` verifica os requisitos funcionais implementados.

Para iniciar a interface gráfica, execute:

```bash
java TelaBiblioteca
```

A interface requer um ambiente com suporte gráfico.

## 11. Requisitos e verificações

| Requisito | Implementação | Verificação |
|---|---|---|
| RF01 — Cadastro e consulta de livros | `Biblioteca.cadastrarLivro()` e `Biblioteca.buscarLivro()` | `TesteRequisitos`: livro cadastrado encontrado |
| RF02 — Cadastro de leitores | `Biblioteca.cadastrarLeitor()` e `Biblioteca.buscarLeitor()` | `TesteRequisitos`: leitor cadastrado encontrado |
| RF03 — Consulta de disponibilidade | `Livro.estaDisponivel()` e `Biblioteca.buscarLivro()` | `TesteRequisitos`: disponibilidade inicial e livro inexistente |
| RF04 — Devolução de livros | `Biblioteca.devolver()` e `Emprestimo.registrarDevolucao()` | `TesteRequisitos`: devolução aceita, livro disponível e segunda devolução recusada |
| RF05 — Empréstimo de livros | `Biblioteca.emprestar()` e `Emprestimo.realizarEmprestimo()` | `TesteRequisitos`: empréstimo aceito, indisponibilidade e respeito ao limite |
| RF06 — Reserva de livros | Ainda não implementado | Não há teste de reserva |

Os testes também verificam recusas para livro inexistente, matrícula inexistente e leitor que atingiu o limite de empréstimos, incluindo a preservação do estado dos objetos após as recusas.

Na última execução de `TesteRequisitos`, foram aprovadas 14 verificações, com 0 falhas.

## 12. O que ainda não faz

- **HU05 — Empréstimos atrasados:** o sistema registra as datas de retirada e devolução, mas ainda não identifica automaticamente empréstimos atrasados.
- **HU06 / RF06 — Reservas:** o sistema ainda não permite reservar livros indisponíveis.
- **RNF02 — Controle de acesso:** ainda não há autenticação nem verificação de permissões para garantir que somente bibliotecários alterem o acervo.
- **Verificação da interface gráfica:** a conexão dos botões foi implementada, mas ainda falta confirmar visualmente o funcionamento completo da janela no ambiente gráfico.

## Uso de inteligência artificial

Utilizei o ChatGPT como apoio na elaboração dos testes de requisitos e na organização da documentação do projeto. Revisei os testes executando-os no ambiente de desenvolvimento para conferir os resultados apresentados.