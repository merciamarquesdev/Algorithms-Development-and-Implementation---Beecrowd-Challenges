import java.util.Scanner;
import java.lang.Math; 

public class Main {
    static int[] C = new int[200010];

    public static int multMod(int a, int b, int n) {
        long la = a;
        long lb = b; 
        int mod = (int) ((la * lb) % n);
        return mod;
    }

    public static int exp(int a, int b, int n) {
        if (b == 0) {
            return 1;
        } else if (b % 2 != 0) {
            return multMod(exp(a, b - 1, n), a, n);
        } else {
            int x = exp(a, b / 2, n);
            return multMod(x, x, n);
        }
    }

    public static int[] geraCrivo(int n, int[] C) {
        for (int i = 1; i <= n; i++) {
            C[i] = i;
        }
        int t = 2;
        for (int i = 1; i <= (int) n/2; i++) {
            C[t] = 2;
            t += 2;
        }
        int s = (int) Math.abs(Math.sqrt(n));
        for (int i = 3; i <= s ; i++) {
            if (C[i] == i) {
                t = i * i;
                int d = i + i;
                while (t <= n) {
                    if (C[t] == t) {
                        C[t] = i;
                    }
                    t += d;
                }
            }
        }
        return C;
    }

    public static int[] carmichael(int n, int[] crivo, int[] carm) {
        for (int i = 2; i <= n; i++) {
            carm[i] = carm[i - 1];
            if (crivo[i] != i) {
                boolean aux = false;
                for (int j = 2; j < i; j++) {
                    if (j != exp(j, i, i)) {
                        aux = true;
                        break;
                    }
                }
                if (!aux) {
                    carm[i] += 1;
                }
            }
        }
        return carm;
    }

    public static void primoConsideracao(int[] C) {
        int crivoTamanho = 200000;
        int[] crivo = geraCrivo(crivoTamanho, C);
        int[] carm = new int[200010];
        carm = carmichael(200000, crivo, carm);
        Scanner scanner = new Scanner(System.in);
        int nCasos = scanner.nextInt();
        while (nCasos > 0) {
            int p = scanner.nextInt();
            int q = scanner.nextInt();
            System.out.println(carm[q] - carm[p]);
            nCasos -= 1;
        }
        scanner.close();
    }

    public static void main(String[] args) {
        primoConsideracao(C);
    }
}
