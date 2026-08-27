/*
 * Disciplina: 2026-PS
 * Estudante: [SeuNome]
 * Data: [AAAA.MM.DD]
 * Projeto: aula32-projeto-secretaria
 * Arquivo: Aluno.java
 */

// A CLASSE E O MOLDE DA FICHA.
// Ela nao guarda os dados de ninguém: descreve o que TODA ficha de aluno
// tem (nome, matricula, curso) e o que ela sabe fazer. Cada "new Aluno(...)"
// no Main cria uma ficha nova a partir deste molde.
// Regra de Java: o arquivo tem o mesmo nome da classe publica - Aluno.java.

public class Aluno {

    // ATRIBUTOS: os campos internos da ficha.
    // "private" - so o codigo desta classe mexe neles de fora. De fora ninguem
    // escreve diretamente, tem que passar pelos metodos publicos la abaixo.
    private String nome;
    private String matricula;
    private String curso;
    private String cidade; // <-- o campo EXTRA DESTE exemplo; o seu e outro

    // CONSTRUTOR: todo mundo no "new" e preenche a ficha.
    // E o "__init__" de voces, em Java. Tem o mesmo nome da classe e nao
    // devolve tipo de retorno. Os valores chegam de fora, entre parenteses.
    public Aluno(String nome, String matricula, String curso, String cidade) {
        // "this" = ESTA ficha aqui (o self do Java).
        // this.nome e o atributo da ficha; nome, sozinho, e o parametro
        // que acabou de chegar. Sao duas coisas, Strings com o mesmo nome.
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
        this.cidade = cidade;
    }

    // GETTERS: as janelas de leitura da ficha.
    // Devolvem o valor guardado sem deixar ninguém de fora alterar.
    // Padrao do nome: get + Atributo, com a primeira letra maiuscula.

    public String getNome() {
        return nome;
    }

    public String getMatricula() {
        return matricula;
    }

    public String getCurso() {
        return curso;
    }

    public String getCidade() {
        return cidade;
    }

    // SETTERS: a unica porta de entrada para mudar um dado da ficha.
    // Hoje eles so trocam o valor, mas aqui alguem que um dia entra a regra
    // ("nome vazio nao vale", "curso tem que existir").
    // Repare que nao existe setMatricula: matricula continua na mao do programa,
    // por decisao do projeto. Se retirar, ninguem altera.

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    // toString: como a ficha se apresenta quando alguem manda imprimi-la.
    // Sem ele, System.out.println(aluno) mostra Aluno@7ad041f3.
    // O @Override avisa o compilador: estou trocando um metodo que toda
    // classe ja tem por uma versao minha.
    @Override
    public String toString() {
        return matricula + " | " + nome + " | " + curso + " | " + cidade;
    }
}