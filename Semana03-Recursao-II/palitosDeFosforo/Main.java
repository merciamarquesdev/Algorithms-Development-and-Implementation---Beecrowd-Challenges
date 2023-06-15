
import java.util.Scanner;

public class Main {
    static long [][]resultado = new long[19][127];
    public static void Q(int n,int k){
        long totalPalitos = 0;
        for( int i = 2; i < 8; i++) {
            if(n-i >= 0){
                if (resultado[k-1][n-i] == -1){
                    Q(n-i,k-1);
                }
                if (i == 5 || i == 6){
                    totalPalitos += 3 * resultado[k-1][n-i];
                }
                else {
                    totalPalitos += resultado[k-1][n-i];
                }
            }
        }
        resultado[k][n] = totalPalitos;
    }

    public static void main(String[] args) {

        for( int linha = 0; linha < resultado.length; linha++) {
            for( int coluna = 0; coluna < resultado[linha].length; coluna++) {
                resultado[linha][coluna] = -1;
            }
        }

        for( int linha = 0; linha < resultado.length; linha++) {
            resultado[linha][0] = 0;
            resultado[linha][1] = 0;
        }

        for( int coluna = 0; coluna < resultado[0].length; coluna++) {
        resultado[0][coluna] = 1;
        }


        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();

        while (nCasos > 0) {
            int n = input.nextInt();
            int k = input.nextInt();
            if(n > 126){
                n = 126;
            }
            Q(n,k);
            if (k == 1){
                System.out.println(resultado[k][n]);
            }
            else {
                int a, b;
                if (k-1 < 0) {
                    a = 0;
                } else {
                    a =  k-1;
                }
                if (n-6 < 0) {
                    b = 0;
                }
                else {
                    b = n-6;
                }
                System.out.println(resultado[k][n] - resultado[a][b]);
            }

            nCasos -= 1;
        }
        input.close();
    }
}
