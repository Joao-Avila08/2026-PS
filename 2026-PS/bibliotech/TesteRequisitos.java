
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

        Livro domCasmurro = biblioteca.buscarLivro("Dom Casmurro");
        Livro capitaes = biblioteca.buscarLivro("Capitaes da Areia");
        Leitor pedro = biblioteca.buscarLeitor("2026010");

        // RF01 — cadastrar e buscar livros
        verificar("RF01 - livro cadastrado encontrado",
            domCasmurro != null);

        // RF02 — cadastrar e buscar leitores
        verificar("RF02 - leitor cadastrado encontrado",
            biblioteca.buscarLeitor("2026011") != null);

        // RF03 — disponibilidade e recusas
        verificar("RF03 - livro novo esta disponivel",
            domCasmurro.estaDisponivel());

        verificar("RF03 - livro inexistente nao e encontrado",
            biblioteca.buscarLivro("O Cortico") == null);

        boolean livroDisponivelAntes = domCasmurro.estaDisponivel();
        int livrosPedroAntes = pedro.getLivrosEmMaos();

        verificar("RF05 - titulo inexistente e recusado",
            !biblioteca.emprestar("O Cortico", "2026010"));

        verificar("RF05 - recusa por titulo nao muda o livro",
            domCasmurro.estaDisponivel() == livroDisponivelAntes);

        verificar("RF05 - recusa por titulo nao muda o leitor",
            pedro.getLivrosEmMaos() == livrosPedroAntes);

        livroDisponivelAntes = capitaes.estaDisponivel();
        livrosPedroAntes = pedro.getLivrosEmMaos();

        verificar("RF05 - matricula inexistente e recusada",
            !biblioteca.emprestar("Capitaes da Areia", "9999999"));

        verificar("RF05 - recusa por matricula nao muda o livro",
            capitaes.estaDisponivel() == livroDisponivelAntes);

        verificar("RF05 - recusa por matricula nao muda o leitor",
            pedro.getLivrosEmMaos() == livrosPedroAntes);

        // RF05 — emprestimo e limite do leitor
        verificar("RF05 - primeiro emprestimo aceito",
            biblioteca.emprestar("Dom Casmurro", "2026010"));

        verificar("RF05 - livro emprestado fica indisponivel",
            !domCasmurro.estaDisponivel());

        verificar("RF05 - leitor no limite tem novo emprestimo recusado",
            !biblioteca.emprestar("Capitaes da Areia", "2026010"));

        verificar("RF05 - recusa preserva disponibilidade do segundo livro",
            capitaes.estaDisponivel());

        verificar("RF05 - recusa preserva quantidade de emprestimos do leitor",
            pedro.getLivrosEmMaos() == 1);

        // RF04 — devolucao
        verificar("RF04 - devolucao de livro emprestado aceita",
            biblioteca.devolver("Dom Casmurro"));

        verificar("RF04 - livro devolvido fica disponivel",
            domCasmurro.estaDisponivel());

        verificar("RF04 - segunda devolucao e recusada",
            !biblioteca.devolver("Dom Casmurro"));

        // Prazo de devolucao — sete dias apos a retirada
        Livro livroPrazo = new Livro("Livro do Prazo", "Autor Teste", 2026);
        Leitor leitorPrazo = new Leitor("Leitor Teste", "2026012", 2);
        Emprestimo emprestimoPrazo = new Emprestimo(livroPrazo, leitorPrazo);

        boolean emprestimoRealizado = emprestimoPrazo.realizarEmprestimo();

        verificar("Prazo - devolucao prevista 7 dias depois da retirada",
            emprestimoRealizado
            && emprestimoPrazo.getDataPrevistaDevolucao() != null
            && emprestimoPrazo.getDataPrevistaDevolucao().equals(
                emprestimoPrazo.getDataRetirada().plusDays(7)
            ));

        verificar("Prazo - data prevista aparece no toString",
            emprestimoRealizado
            && emprestimoPrazo.toString().contains(
                emprestimoPrazo.getDataPrevistaDevolucao().toString()
            ));

        System.out.println();
        System.out.println("=== RESULTADO DOS TESTES ===");
        System.out.println("Passaram: " + passou);
        System.out.println("Falharam: " + falhou);
        System.out.println("Total: " + (passou + falhou));
    }
}
