import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nCasos = scanner.nextInt();
        while (nCasos > 0) {
            int c = scanner.nextInt();
            int l = scanner.nextInt();
            int[] p = new int[c + 1];
            for (int i = 1; i <= c; i++) {
                p[i] = scanner.nextInt();
            }
            int[] k = new int[l + 1];
            for (int i = 0; i <= l; i++) {
                k[i] = -1;
            }
            char resultado = mochila(c, l, p, k);
            System.out.println(resultado);
            nCasos--;
        }
    }

    public static char mochila(int c, int l, int[] p, int[] k) {
        k[0] = 0;
        for (int q = 1; q <= c; q++) {
            for (int j = l - p[q] - 1; j >= 0; j--) {
                if (k[j] >= 0 && k[j + p[q]] == -1) {
                    k[j + p[q]] = q;
                }
            }
        }
        int maximo = 0;
        int i = k.length - 1;
        while (i > 0) {
            if (k[i] != -1) {
                maximo += p[k[i]];
                i -= p[k[i]];
            } else {
                i -= 1;
            }
        }
        int total = 0;
        for (int j = 1; j <= c; j++) {
            total += p[j];
        }
        if (total - maximo <= l) {
            return 'S';
        } else {
            return 'N';
        }
    }
}
