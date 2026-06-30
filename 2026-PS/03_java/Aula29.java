import java.util.ArrayList;

public class Main {

    public static double calcularMedia(double[] notas) {
        double soma = 0;

        for (double nota : notas) {
            soma += nota;
        }

        return soma / notas.length;
    }

    public static int contarAprovados(double[] notas) {
        int contador = 0;

        for (double nota : notas) {
            if (nota >= 6.0) {
                contador++;
            }
        }

        return contador;
    }

    public static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    public static void listarProdutos(ArrayList<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println((i + 1) + " - " + lista.get(i));
        }
    }

    public static int maiorValor(int[] valores) {
        if (valores.length == 0) {
            throw new IllegalArgumentException("O array não pode estar vazio.");
        }

        int maior = valores[0];

        for (int valor : valores) {
            if (valor > maior) {
                maior = valor;
            }
        }

        return maior;
    }

    public static int maiorValor(int a, int b) {
        return (a > b) ? a : b;
    }

    public static int contarAcimaDaMedia(double[] notas) {
        double media = calcularMedia(notas);
        int contador = 0;

        for (double nota : notas) {
            if (nota > media) {
                contador++;
            }
        }

        return contador;
    }

    public static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);

        if (media >= 6.0) {
            System.out.println("Situação: APROVADA");
        } else {
            System.out.println("Situação: EM RECUPERAÇÃO");
        }

        System.out.println("Acima da média: " + contarAcimaDaMedia(notas));
    }

    public static void main(String[] args) {
        double[] notas = {7.0, 5.0, 9.0, 6.0};

        System.out.println("=== Exercício 1 ===");
        System.out.println("Média = " + calcularMedia(notas));

        System.out.println("\n=== Exercício 2 ===");
        System.out.println("Aprovados = " + contarAprovados(notas));

        System.out.println("\n=== Exercício 3 ===");
        ArrayList<String> produtos = new ArrayList<>();

        adicionarProduto(produtos, "Pizza");
        adicionarProduto(produtos, "Suco");

        listarProdutos(produtos);

        System.out.println("\n=== Exercício 4 ===");
        System.out.println("Maior valor do array: " + maiorValor(new int[]{3, 9, 5}));
        System.out.println("Maior entre dois números: " + maiorValor(12, 7));

        System.out.println("\n=== Exercício 5 ===");
        exibirBoletim(notas);
    }
}
