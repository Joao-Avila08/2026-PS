public class TesteInsercao {
    public static void main(String[] args) {
        LivroDAO dao = new LivroDAO();

        System.out.println("Livro 1 inserido: " +
            dao.adicionarLivro("O Hobbit", "J. R. R. Tolkien", 1937));

        System.out.println("Livro 2 inserido: " +
            dao.adicionarLivro("1984", "George Orwell", 1949));

        System.out.println("Livro 3 inserido: " +
            dao.adicionarLivro("A Revolução dos Bichos", "George Orwell", 1945));
    }
}
