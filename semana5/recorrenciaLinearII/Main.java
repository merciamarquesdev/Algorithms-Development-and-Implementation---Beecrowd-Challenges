import java.util.Scanner;

public class Main {
    static long num = 1000000007;

    public static long somaMod(long a,long b){
        return (a+b)%num;
    }

    public static long multMod(long a, long b){
        return (a*b)%num;
    }

    public static long[][] matrizIdentidade(int k) {
        long[][] identidade = new long[k][k];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                identidade[i][j] = (i == j) ? 1 : 0;
            }
        }
        return identidade;
    }

    public static long[][] multiplicaMatrizes(long[][] a, long[][] b, int k) {
        long[][] r = new long[k][k];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                for (int z = 0; z < k; z++) {
                    r[i][j] = somaMod(r[i][j], multMod(a[i][z], b[z][j]));
                }
            }
        }
        return r;
    }

    public static long[][] exp(long[][] matrizA, long n, int k) {
        long[][] b = matrizA;
        if(n <= 0){
            return matrizIdentidade(k);
        } else if(n%2 != 0){
            long[][] a = exp(b, n-1, k);
            return multiplicaMatrizes(a, b, k);
        } else {
            long[][] x = exp(b, n/2, k);
            return multiplicaMatrizes(x, x, k);
        }
    }

    public static long T(long n, long[][] matrizA, long[] linha3, int k) {
        for (int i = 0; i < k; i++) {
            if (n == i) {
                return linha3[i];
            }
        }
        long[][] a = exp(matrizA, n-(k-1), k);
        long[] b = new long[k];
        for (int i = 0; i < k; i++) {
            b[i] = linha3[k-1-i];
        }
        long resultado = 0;
        for (int i = 0; i < k; i++) {
            resultado = somaMod(resultado, multMod(a[0][i], b[i]));
        }
        return resultado;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();
        input.nextLine();
        while (nCasos > 0) {
            String[] linha1 = input.nextLine().split(" ");
            long n = Long.parseLong(linha1[0]);
            int k = Integer.parseInt(linha1[1]);
            long[] linha2 = new long[k];
            String[] linha2Str = input.nextLine().split(" ");
            for (int i = 0; i < k; i++) {
                linha2[i] = Long.parseLong(linha2Str[i]);
            }
            long[] linha3 = new long[k];
            String[] linha3Str = input.nextLine().split(" ");
            for (int i = 0; i < k; i++) {
                linha3[i] = Long.parseLong(linha3Str[i]);
            }
            long[][] matrizA = new long[k][k];
            for (int i = 0; i < k; i++) {
                matrizA[0][i] = linha2[i];
            }
            for (int i = 1; i < k; i++) {
                matrizA[i][i-1] = 1;
            }
            long result = T(n, matrizA, linha3, k);
            System.out.println(result);
            nCasos--;
        }
        input.close();
    }
}
