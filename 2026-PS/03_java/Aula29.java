import java.util.ArrayList;

public class main{

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
        int maior = valores[0];

        for (int valor : valores) {
            if (valor > maior) {
                maior = valor;
            }
        }

        return maior;
    }

    public static int maiorValor(int a, int b) {
        if (a > b) {
            return a;
        }

        return b;
    }

    public static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);

        if (media >= 6.0) {
            System.out.println("Situação: Aprovada");
        } else {
            System.out.println("Situação: Em recuperação");
        }
    }

    public static void main(String[] args) {
        double[] notas = {7.0, 5.0, 9.0, 6.0};

        System.out.println("Média = " + calcularMedia(notas));
        System.out.println("Aprovados = " + contarAprovados(notas));

        ArrayList<String> produtos = new ArrayList<>();

        adicionarProduto(produtos, "Pizza");
        adicionarProduto(produtos, "Suco");

        listarProdutos(produtos);

        System.out.println("Maior valor do array: " + maiorValor(new int[]{3, 9, 5}));
        System.out.println("Maior entre dois números: " + maiorValor(12, 7));

        exibirBoletim(notas);
    }
}