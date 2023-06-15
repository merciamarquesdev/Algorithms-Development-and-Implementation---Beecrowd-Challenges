import java.util.Scanner;

public class Main {

public static int modSoma(int a, int b) {
    int z = 1000000007;
    return (a + b)%z;
}

public static int[][] criaMatriz(int t, int m, int n) {
    int[][] matriz = new int[n - m + 3][t + 1];
    for (int i = 0; i < n - m + 3; i++) {
        for (int j = 0; j < t + 1; j++) {
            matriz[i][j] = 0;
        }
    }
    return matriz;
}

public static int T(int[][] matriz, int t, int m, int n) {
    int somatorio = 0;
    for (int coluna = 1; coluna <= t; coluna++) {
        for (int linha = 0; linha <= n - m + 2; linha++) {
            if (coluna == 1 && linha >= 1 && linha <= n - m + 1) {
                matriz[linha][coluna] = 1;
            } else if (linha < 1 || linha > n - m + 1) {
                matriz[linha][coluna] = 0;
            } else if (coluna > 1 && linha >= 1 && linha <= n - m + 1) {
                matriz[linha][coluna] = modSoma(matriz[linha - 1][coluna - 1], matriz[linha + 1][coluna - 1]);
            }
        }
    }
    for (int i = 0; i <= n - m + 2; i++) {
        somatorio = modSoma(matriz[i][t], somatorio);
    }
    return somatorio;
}

public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int nCasos = sc.nextInt();
    while (nCasos > 0) {
        int t = sc.nextInt();
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[][] matriz = criaMatriz(t, m, n);
        int resultado = T(matriz, t, m, n);
        System.out.println(resultado);
        nCasos--;
    }
    sc.close();
}
}
