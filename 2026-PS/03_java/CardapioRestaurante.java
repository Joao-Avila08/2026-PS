import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("=================================");
        System.out.println("       DEV BITES RESTAURANTE     ");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$  8,00");
        System.out.println("4 - Café ............... R$  5,00");
        System.out.println("5 - Batata Frita ....... R$ 12,00");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        String itemEscolhido = "";
        double precoUnitario = 0.0;
        boolean opcaoValida = true;

        switch (opcao) {
            case 1:
                itemEscolhido = "X-Burguer";
                precoUnitario = 18.00;
                break;
            case 2:
                itemEscolhido = "Pizza";
                precoUnitario = 35.00;
                break;
            case 3:
                itemEscolhido = "Suco Natural";
                precoUnitario = 8.00;
                break;
            case 4:
                itemEscolhido = "Café";
                precoUnitario = 5.00;
                break;
            case 5:
                itemEscolhido = "Batata Frita";
                precoUnitario = 12.00;
                break;
            default:
                System.out.println("\n[ERRO] Opção inválida. Digite um número de 1 a 5.");
                opcaoValida = false;
                break;
        }

        if (opcaoValida) {
            System.out.print("Digite a quantidade desejada: ");
            int quantidade = entrada.nextInt();

            double valorTotal = precoUnitario * quantidade;

            System.out.println("\n=================================");
            System.out.println("        RESUMO DO PEDIDO         ");
            System.out.println("=================================");
            System.out.println("Item: " + itemEscolhido);
            System.out.printf("Preço unitário: R$ %.2f\n", precoUnitario);
            System.out.println("Quantidade: " + quantidade);
            System.out.println("---------------------------------");
            System.out.printf("VALOR TOTAL: R$ %.2f\n", valorTotal);
            System.out.println("=================================");
        }

        entrada.close();
    }
}