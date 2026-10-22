
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

A classe registra as datas de retirada, devolução e devolução prevista, além de controlar se o empréstimo está ativo.

A data prevista de devolução é calculada para sete dias após a retirada, utilizando `LocalDate.plusDays(7)`. Essa data pode ser consultada pelo método `getDataPrevistaDevolucao()` e aparece na representação textual do empréstimo, fornecida por `toString()`.

As principais operações são:

- `realizarEmprestimo()`: verifica se o livro está disponível e se o leitor pode pegar outro livro antes de registrar o empréstimo.
- `registrarDevolucao()`: registra a devolução e atualiza a disponibilidade do livro e a quantidade de livros com o leitor.
- `estaAtivo()`: informa se o empréstimo continua ativo.
- `getDataPrevistaDevolucao()`: retorna a data prevista para a devolução.

O método `realizarEmprestimo()` impede empréstimos inválidos sem alterar os dados do livro ou do leitor. Já `registrarDevolucao()` verifica se o empréstimo está ativo, evitando que uma segunda devolução altere os dados novamente.

A classe `TesteEmprestimo` verifica situações relacionadas ao empréstimo e à devolução. A classe `TesteRequisitos` também verifica as recusas de operações inválidas, a preservação dos estados e o cálculo do prazo de sete dias.

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

A classe `TesteBiblioteca` verifica o funcionamento integrado do sistema, incluindo consultas ao acervo, cadastro e busca de leitores, empréstimos aceitos e recusados, controle do limite de empréstimos e devoluções.

A classe `TesteRequisitos` verifica os requisitos funcionais implementados, incluindo a disponibilidade dos livros, as recusas de operações inválidas, a preservação dos dados após recusas e o prazo previsto de devolução.

A interface gráfica `TelaBiblioteca` foi testada, e os botões de empréstimo, devolução e atualização do acervo funcionaram conforme esperado, atualizando as informações exibidas após as operações.

Na última execução de `TesteRequisitos`, foram aprovadas 20 verificações, com 0 falhas.

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
| RF05 — Empréstimo de livros | `Biblioteca.emprestar()` e `Emprestimo.realizarEmprestimo()` | `TesteRequisitos`: empréstimo aceito, indisponibilidade, recusas e respeito ao limite |
| RF06 — Reserva de livros | Ainda não implementado | Não há teste de reserva |

Os testes também verificam recusas para livro inexistente, matrícula inexistente e leitor que atingiu o limite de empréstimos, incluindo a preservação do estado dos objetos após as recusas.

A classe `TesteRequisitos` verifica ainda se a data prevista de devolução corresponde a sete dias após a retirada e se essa data aparece no método `toString()`.

Na última execução de `TesteRequisitos`, foram aprovadas **20 verificações, com 0 falhas**.

## 12. O que ainda não faz

- **HU05 — Empréstimos atrasados:** o sistema registra as datas de retirada e devolução prevista, mas ainda não identifica automaticamente os empréstimos atrasados.
- **HU06 / RF06 — Reservas:** o sistema ainda não permite reservar livros indisponíveis.
- **RNF02 — Controle de acesso:** ainda não há autenticação nem verificação de permissões para garantir que somente bibliotecários alterem o acervo.
- **Verificação da interface gráfica:** a conexão dos botões foi implementada, mas ainda falta confirmar visualmente o funcionamento completo da janela no ambiente gráfico.

## Uso de inteligência artificial

Utilizei o ChatGPT como apoio na elaboração dos testes de requisitos e na organização da documentação do projeto. Revisei os testes executando-os no ambiente de desenvolvimento para conferir os resultados apresentados.

## 13. Verificações adicionais — Aula 41

A classe `Emprestimo` registra a data da retirada e calcula a data prevista de devolução para sete dias depois, utilizando `LocalDate.plusDays(7)`.

A data prevista pode ser consultada pelo método `getDataPrevistaDevolucao()` e também aparece no método `toString()`.

O arquivo `TesteRequisitos.java` contém 20 verificações, incluindo:

- Recusa de empréstimo para título inexistente.
- Recusa de empréstimo para matrícula inexistente.
- Conferência de que o livro e o leitor permanecem inalterados após essas recusas.
- Verificação do limite de empréstimos do leitor.
- Verificação da devolução e da disponibilidade do livro.
- Verificação do prazo de sete dias e da exibição da data prevista.

Resultado da última execução: **20 testes passaram e 0 falharam**.
## 14. Persistência de dados — Aula 42

O BiblioTech utiliza MariaDB para armazenar os livros de forma persistente, mantendo os registros mesmo depois que o programa Java é encerrado.

### Banco de dados

O banco utilizado é `bibliotech`, com a tabela `livros`, que possui os seguintes campos:

- `id`: identificador único gerado automaticamente.
- `titulo`: título do livro.
- `autor`: nome do autor.
- `ano`: ano de publicação.

### Conexão JDBC

A classe `Conexao` estabelece a conexão entre Java e MariaDB utilizando o driver JDBC. As credenciais são obtidas pelas variáveis de ambiente `DB_USER` e `DB_PASSWORD`, evitando deixar a senha diretamente no código.

### Operações de persistência

A classe `LivroDAO` realiza as operações no banco de dados:

- `adicionarLivro()`: cadastra um livro.
- `atualizarLivro()`: atualiza os dados de um livro.
- `excluirLivro()`: remove um livro.

As operações utilizam consultas preparadas (`PreparedStatement`) e retornam `true` quando algum registro é afetado e `false` quando nenhum registro é alterado ou ocorre uma falha.

### Testes realizados

A classe `TesteConexao` verifica a conexão com o banco. A classe `TesteLivroDAO` verifica a inclusão, a atualização e a exclusão de livros, além de testar operações com identificadores inexistentes.

Nos testes realizados, os três livros foram inseridos com sucesso. Em seguida, o título de um livro foi atualizado, outro foi excluído e as operações com o identificador `999999` retornaram `false`. A consulta final confirmou que os dois livros restantes continuaram armazenados após o encerramento do programa Java.

### Como executar os testes

Na pasta `bibliotech`, configure as credenciais no terminal:

```bash
export DB_USER=bibliotech
read -rs -p "Senha do banco: " DB_PASSWORD
echo
export DB_PASSWORD