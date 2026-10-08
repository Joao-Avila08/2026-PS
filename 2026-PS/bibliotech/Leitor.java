public class Leitor extends Usuario {

    private int limiteEmprestimos;
    private int livrosEmMaos;

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula);
        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEmMaos = 0;
    }

    public int getLimiteEmprestimos() {
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos() {
        return livrosEmMaos;
    }

    public boolean podePegarEmprestado() {
        return livrosEmMaos < limiteEmprestimos;
    }

    public void pegouLivro() {
        livrosEmMaos++;
    }

    public void devolveuLivro() {
        livrosEmMaos--;
    }

    public String toString() {
        return "Leitor " + getNome() + " (" + getMatricula() + ") - "
                + livrosEmMaos + " de " + limiteEmprestimos + " livros";
    }
}