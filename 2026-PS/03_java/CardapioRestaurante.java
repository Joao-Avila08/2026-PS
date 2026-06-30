```java
import java.util.Random;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random random = new Random();

        double valorTotal = 0;

        String resumoPedido = "";

        boolean continuar = true;

        while (continuar) {

            System.out.println("=================================");
            System.out.println("       DEV BITES RESTAURANTE     ");
            System.out.println("=================================");
            System.out.println("1 - X-Burguer .......... R$ 18,00");
            System.out.println("2 - Pizza .............. R$ 35,00");
            System.out.println("3 - Suco Natural ....... R$  8,00");
            System.out.println("4 - Café ............... R$  5,00");
            System.out.println("5 - Batata Frita ....... R$ 12,00");
            System.out.println("6 - Finalizar Pedido");
            System.out.println("=================================");

            System.out.print("Escolha uma opção: ");
            int opcao = entrada.nextInt();

            if (opcao == 6) {
                break;
            }

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
                    System.out.println("\n[ERRO] Opção inválida.");
                    opcaoValida = false;
                    break;
            }

            if (opcaoValida) {

                System.out.println("Item: " + itemEscolhido);
                System.out.printf("Preço: R$ %.2f%n", precoUnitario);

                System.out.print("Digite a quantidade desejada: ");
                int quantidade = entrada.nextInt();

                double subtotal = precoUnitario * quantidade;

                valorTotal += subtotal;

                resumoPedido += quantidade + "x "
                        + itemEscolhido
                        + " .... R$ "
                        + String.format("%.2f", subtotal)
                        + "\n";

                System.out.println("Item adicionado ao pedido!");
            }

            System.out.println("\nDeseja continuar comprando?");
            System.out.println("1 - Sim");
            System.out.println("2 - Finalizar");

            int escolha = entrada.nextInt();

            if (escolha == 2) {
                continuar = false;
            }
        }

        System.out.println("\n=================================");
        System.out.println("        RESUMO DO PEDIDO         ");
        System.out.println("=================================");

        System.out.println(resumoPedido);

        System.out.println("---------------------------------");
        System.out.printf("VALOR TOTAL: R$ %.2f%n", valorTotal);

        System.out.println("\nForma de pagamento:");
        System.out.println("1 - Dinheiro");
        System.out.println("2 - Cartão");
        System.out.println("3 - PIX");

        System.out.print("Escolha: ");
        int pagamento = entrada.nextInt();

        if (pagamento >= 1 && pagamento <= 3) {

            System.out.println("\nPagamento realizado com sucesso!");

            int numeroPedido = random.nextInt(900) + 100;

            System.out.println("Pedido Nº " + numeroPedido);
            System.out.println("Aguarde a chamada do seu pedido.");

        } else {
            System.out.println("Forma de pagamento inválida.");
        }

        entrada.close();
    }
}
```
