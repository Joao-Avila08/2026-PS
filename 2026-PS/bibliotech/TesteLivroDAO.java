public class TesteLivroDAO {
    public static void main(String[] args) {
        LivroDAO dao = new LivroDAO();

        boolean atualizado = dao.atualizarLivro(
            1,
            "O Pequeno Príncipe - Edição Revisada",
            "Antoine de Saint-Exupéry",
            1943
        );

        boolean excluido = dao.excluirLivro(3);

        boolean atualizacaoInvalida = dao.atualizarLivro(
            999999, "Livro Inexistente", "Autor", 2000
        );

        boolean exclusaoInvalida = dao.excluirLivro(999999);

        System.out.println("Livro atualizado: " + atualizado);
        System.out.println("Livro excluído: " + excluido);
        System.out.println("Atualização de ID inexistente: " + atualizacaoInvalida);
        System.out.println("Exclusão de ID inexistente: " + exclusaoInvalida);
    }
}
