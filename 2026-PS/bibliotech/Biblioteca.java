import java.util.ArrayList;

public class Biblioteca {
    private ArrayList<Livro> livros;
    private ArrayList<Leitor> leitores;
    private ArrayList<Emprestimo> emprestimos;

    public Biblioteca() {
        livros = new ArrayList<>();
        leitores = new ArrayList<>();
        emprestimos = new ArrayList<>();
    }

    public void cadastrarLivro(Livro livro) {
        if (livro != null) {
            livros.add(livro);
        }
    }

    public boolean cadastrarLeitor(Leitor leitor) {
        if (leitor == null) {
            return false;
        }

        for (Leitor cadastrado : leitores) {
            if (cadastrado.getMatricula().equals(leitor.getMatricula())) {
                return false;
            }
        }

        leitores.add(leitor);
        return true;
    }

    public void listarAcervo() {
        System.out.println("--- Acervo ---");

        for (Livro livro : livros) {
            System.out.println(livro);
        }
    }

    public String obterAcervoComoTexto() {
        if (livros.isEmpty()) {
            return "Nenhum livro cadastrado.";
        }

        String texto = "";

        for (int i = 0; i < livros.size(); i++) {
            texto = texto + livros.get(i) + "\n";
        }

        return texto;
    }

    public Livro buscarLivro(String titulo) {
        for (Livro livro : livros) {
            if (livro.getTitulo().equals(titulo)) {
                return livro;
            }
        }

        return null;
    }

    public Leitor buscarLeitor(String matricula) {
        for (Leitor leitor : leitores) {
            if (leitor.getMatricula().equals(matricula)) {
                return leitor;
            }
        }

        return null;
    }

    public boolean emprestar(String titulo, String matricula) {
        Livro livro = buscarLivro(titulo);
        Leitor leitor = buscarLeitor(matricula);

        if (livro == null || leitor == null) {
            return false;
        }

        Emprestimo emprestimo = new Emprestimo(livro, leitor);

        if (emprestimo.realizarEmprestimo()) {
            emprestimos.add(emprestimo);
            return true;
        }

        return false;
    }

    public boolean devolver(String titulo) {
        for (Emprestimo emprestimo : emprestimos) {
            if (emprestimo.estaAtivo()
                    && emprestimo.getLivro().getTitulo().equals(titulo)) {
                return emprestimo.registrarDevolucao();
            }
        }

        return false;
    }

    public void listarEmprestimos() {
        System.out.println("--- Emprestimos ---");

        for (Emprestimo emprestimo : emprestimos) {
            System.out.println(emprestimo);
        }
    }

    public void listarLivrosDoLeitor(String matricula) {
        System.out.println("--- Livros com a matricula " + matricula + " ---");

        for (Emprestimo emprestimo : emprestimos) {
            if (emprestimo.estaAtivo()
                    && emprestimo.getLeitor().getMatricula().equals(matricula)) {
                System.out.println(emprestimo.getLivro());
            }
        }
    }
}