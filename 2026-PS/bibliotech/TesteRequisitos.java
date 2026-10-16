public class TesteRequisitos {

    private static int passou = 0;
    private static int falhou = 0;

    private static void verificar(String nome, boolean condicao) {
        if (condicao) {
            System.out.println("OK: " + nome);
            passou++;
        } else {
            System.out.println("FALHOU: " + nome);
            falhou++;
        }
    }

    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(
            new Livro("Dom Casmurro", "Machado de Assis", 1899)
        );
        biblioteca.cadastrarLivro(
            new Livro("Capitaes da Areia", "Jorge Amado", 1937)
        );

        biblioteca.cadastrarLeitor(
            new Leitor("Pedro Alves", "2026010", 1)
        );
        biblioteca.cadastrarLeitor(
            new Leitor("Ana Lima", "2026011", 2)
        );

        // RF01 — cadastrar e buscar livros
        verificar("RF01 - livro cadastrado encontrado",
            biblioteca.buscarLivro("Dom Casmurro") != null);

        // RF02 — cadastrar e buscar leitores
        verificar("RF02 - leitor cadastrado encontrado",
            biblioteca.buscarLeitor("2026011") != null);

        // RF03 — disponibilidade e recusas
        verificar("RF03 - livro novo esta disponivel",
            biblioteca.buscarLivro("Dom Casmurro").estaDisponivel());

        verificar("RF03 - livro inexistente nao e encontrado",
            biblioteca.buscarLivro("O Cortico") == null);

        verificar("RF03 - emprestimo de livro inexistente recusado",
            !biblioteca.emprestar("O Cortico", "2026011"));

        verificar("RF03 - matricula inexistente recusada",
            !biblioteca.emprestar("Capitaes da Areia", "9999999"));

        // RF05 — emprestimo e limite do leitor
        verificar("RF05 - primeiro emprestimo aceito",
            biblioteca.emprestar("Dom Casmurro", "2026010"));

        verificar("RF05 - livro emprestado fica indisponivel",
            !biblioteca.buscarLivro("Dom Casmurro").estaDisponivel());

        verificar("RF05 - leitor no limite tem novo emprestimo recusado",
            !biblioteca.emprestar("Capitaes da Areia", "2026010"));

        verificar("RF05 - recusa preserva disponibilidade do segundo livro",
            biblioteca.buscarLivro("Capitaes da Areia").estaDisponivel());

        verificar("RF05 - recusa preserva quantidade de emprestimos do leitor",
            biblioteca.buscarLeitor("2026010").getLivrosEmMaos() == 1);

        // RF04 — devolucao
        verificar("RF04 - devolucao de livro emprestado aceita",
            biblioteca.devolver("Dom Casmurro"));

        verificar("RF04 - livro devolvido fica disponivel",
            biblioteca.buscarLivro("Dom Casmurro").estaDisponivel());

        verificar("RF04 - segunda devolucao e recusada",
            !biblioteca.devolver("Dom Casmurro"));

        System.out.println();
        System.out.println("=== RESULTADO DOS TESTES ===");
        System.out.println("Passaram: " + passou);
        System.out.println("Falharam: " + falhou);
        System.out.println("Total: " + (passou + falhou));
    }
}