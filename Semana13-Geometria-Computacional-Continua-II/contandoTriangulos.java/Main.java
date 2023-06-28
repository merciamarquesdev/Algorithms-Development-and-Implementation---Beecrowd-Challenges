import java.util.Scanner;
import java.lang.Math;

public class Main {

public static double z = 0.000000001;

public static boolean igual(double a, double b) {
    return Math.abs(a - b) <= z;
}

public static boolean menor(double a, double b) {
    return a < b;
}

public static double area(double[] a, double[] b, double[] c) {
    double area = (a[0] * (b[1] - c[1])) - (b[0] * (a[1] - c[1])) + (c[0] * (a[1] - b[1]));
    return Math.abs(area);
}

public static double[] ladosTriangulo(double[] x, double[] y, double[] z) {
    double a = Math.sqrt(Math.pow((x[0] - y[0]), 2) + Math.pow((x[1] - y[1]), 2));
    double b = Math.sqrt(Math.pow((y[0] - z[0]), 2) + Math.pow((y[1] - z[1]), 2));
    double c = Math.sqrt(Math.pow((z[0] - x[0]), 2) + Math.pow((z[1] - x[1]), 2));
    double temp = Math.max(a, Math.max(b, c));
    if (temp == a) {
        a = c;
        c = temp;
    } else if (temp == b) {
        b = c;
        c = temp;
    }
    return new double[] { c, a, b };
}

public static int[] tipoTriangulo(double c, double a, double b, int nr, int na, int no) {
    if (igual(c * c, (a * a + b * b))) {
        nr++;
    } else if (menor(c * c, (a * a + b * b))) {
        na++;
    } else {
        no++;
    }
    return new int[] { nr, na, no };
}

public static void contandoTriangulos() {
    Scanner scanner = new Scanner(System.in);
    int casos = scanner.nextInt();
    while (casos > 0) {
        int nr = 0;
        int na = 0;
        int no = 0;

        int n = scanner.nextInt();
        double[][] pontos = new double[n][2];

        for (int i = 0; i < 2 * n; i += 2) {
            pontos[i / 2][0] = scanner.nextDouble();
            pontos[i / 2][1] = scanner.nextDouble();
        }

        for (int x = 0; x < n - 2; x++) {
            for (int y = x + 1; y < n - 1; y++) {
                for (int z = y + 1; z < n; z++) {
                    if (area(pontos[x], pontos[y], pontos[z]) != 0) { // teste de nao-colinearidade
                        double[] sides = ladosTriangulo(pontos[x], pontos[y], pontos[z]);
                        int[] counts = tipoTriangulo(sides[0], sides[1], sides[2], nr, na, no);
                        nr = counts[0];
                        na = counts[1];
                        no = counts[2];
                    }
                }
            }
        }
        System.out.println(nr + " " + na + " " + no);

        casos--;
    }
    scanner.close();
}

public static void main(String[] args) {
    contandoTriangulos();
}

}