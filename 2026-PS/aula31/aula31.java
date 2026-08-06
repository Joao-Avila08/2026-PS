public class Main {

    // ================= INT =================

    // Soma dos valores (int)
    public static int calculaSomaInt(int[] valores) {
        int soma = 0;

        for(int i = 0; i < valores.length; i++) {
            soma += valores[i];
        }

        return soma;
    }


    // Média dos valores (int)
    public static int calculaMediaInt(int[] valores) {
        int soma = 0;

        for(int i = 0; i < valores.length; i++) {
            soma += valores[i];
        }

        return soma / valores.length;
    }


    // Menor valor (int)
    public static int menorValorInt(int[] valores) {
        int menor = valores[0];

        for(int i = 1; i < valores.length; i++) {
            if(valores[i] < menor) {
                menor = valores[i];
            }
        }

        return menor;
    }


    // Maior valor (int)
    public static int maiorValorInt(int[] valores) {
        int maior = valores[0];

        for(int i = 1; i < valores.length; i++) {
            if(valores[i] > maior) {
                maior = valores[i];
            }
        }

        return maior;
    }


    // Contar acima (int)
    public static int contarAcimaInt(int[] valores, int limite) {
        int contador = 0;

        for(int i = 0; i < valores.length; i++) {
            if(valores[i] > limite) {
                contador++;
            }
        }

        return contador;
    }

}