/*  Disciplina: Programacao de Sistemas
 Aluno: Joao Vitor Gracietti de Avila
 Data: 2026.08.20
 Projeto: Projeto Secretaria
 Arquivo: Main.java
*/
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        ArrayList<Aluno> lista = new ArrayList<Aluno>();
        Scanner teclado = new Scanner(System.in);

        while (true) {
            System.out.println("==========================================");
            System.out.println("   SECRETARIA JOAO VITOR GRACIETTI DE AVILA");
            System.out.println("==========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else {
                System.out.println("Opcao invalida! Vale 0, 1 ou 2.");
            }
        }

        teclado.close();
    }

    // Cadastra uma nova ficha e guarda no gaveteiro
    public static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        Aluno novo = new Aluno(nome, matricula, curso);
        lista.add(novo);

        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

 
    public static void listar(ArrayList<Aluno> lista) {
        if (lista.isEmpty()) {
            System.out.println("Nenhuma ficha cadastrada ainda.");
            return;
        }

        System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---");
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            System.out.println(a.getMatricula() + " | " + a.getNome() + " | " + a.getCurso());
        }
    }
}