import java.util.Scanner;

public class TesteBuscarLivro {
    public static void main(String[] args) {
        LivroDAO dao = new LivroDAO();
        Scanner scanner = new Scanner(System.in);

        int id;

        do {
            System.out.print("Digite o ID do livro (0 para sair): ");
            id = scanner.nextInt();

            if (id != 0) {
                Livro livro = dao.buscarLivroPorId(id);

                if (livro != null) {
                    System.out.println("Livro encontrado:");
                    System.out.println(livro);
                } else {
                    System.out.println("Livro nao encontrado.");
                }
            }
        } while (id != 0);

        scanner.close();
    }
}
