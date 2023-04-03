
import java.util.Scanner;

public class Main {
    public static long fm(int n, int m) {
        if (m == 0 || n == 0) {
            return 0;
        }
        else {
            return fn(n,m) + fm(n,m-1);
        }
    }
    public static long fn(int n, int m){
        if (n == 1) {
            return m;
        }
        else {
            return ((long) n * m) + fn(n - 1, m);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();

        while (nCasos > 0) {
            int n = input.nextInt();
            int m = input.nextInt();
            System.out.println(fm(n, m));
            nCasos -= 1;
        }
        input.close();
    }
}