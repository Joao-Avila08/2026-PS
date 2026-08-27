/*
 Disciplina: Programacao de Sistemas
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
            System.out.println("[3] Buscar aluno");
            System.out.println("[4] Atualizar aluno");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
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
            } else if (opcao.equals("3")) {
                buscar(lista, teclado);
            } else if (opcao.equals("4")) {
                atualizar(lista, teclado);
            } else if (opcao.equals("5")) {
                remover(lista, teclado);
            } else if (opcao.equals("6")) {
                relatorio(lista, teclado);
            } else {
                System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4, 5 ou 6.");
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

        if (buscarPorMatricula(lista, matricula) != null) {
            System.out.println("Ja existe ficha com a matricula " + matricula + "!");
            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        System.out.print("Cidade: ");
        String cidade = teclado.nextLine().trim();

        Aluno novo = new Aluno(nome, matricula, curso, cidade);
        lista.add(novo);

        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha no gaveteiro ainda.");
            return;
        }

        System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---");

        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            System.out.println(a); // a impressao chama o toString sozinha
        }
    }

    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula) {
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);

            if (a.getMatricula().equals(matricula)) {
                return a;
            }
        }

        return null;
    }

    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula procurada: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }

        System.out.println("Achei: " + a);
    }

    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }

        System.out.print("Novo curso de " + a.getNome() + ": ");
        String curso = teclado.nextLine().trim();

        a.setCurso(curso);

        System.out.println("Ficha atualizada: " + a);
    }

    static void remover(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a remover: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }

        System.out.print("Tem certeza que remove " + a.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();

        if (resposta.equals("s")) {
            lista.remove(a);
            System.out.println("Ficha removida.");
        } else {
            System.out.println("Remocao cancelada.");
        }
    }

    // RELATORIO: o padrao preparar -> percorrer -> usar, da Aula 29.
    static void relatorio(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.println("--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + lista.size());

        System.out.print("Contar alunos de qual curso? ");
        String curso = teclado.nextLine().trim();

        // preparar (ANTES do for)
        int contador = 0;

        for (int i = 0; i < lista.size(); i++) { // percorrer
            Aluno a = lista.get(i);

            if (a.getCurso().equals(curso)) {
                contador = contador + 1;
            }
        }

        // usar
        System.out.println("Alunos de " + curso + ": " + contador);
    }
}