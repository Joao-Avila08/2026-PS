import java.sql.Connection;
import java.sql.SQLException;

public class TesteConexao {
    public static void main(String[] args) {
        try (Connection conexao = Conexao.conectar()) {
            System.out.println("Conexao com o MariaDB realizada com sucesso!");
        } catch (SQLException e) {
            System.err.println("Erro na conexao: " + e.getMessage());
        }
    }
}
