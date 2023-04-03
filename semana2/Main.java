
import java.util.Scanner;

public class Main {
    public static long f(long n, long p){
        if (n == p) {
            return 1;
        }
        else{
            return f(n - 1, p) * n / (n - p);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();

        while (nCasos > 0) {
            int n = input.nextInt();
            int p = input.nextInt();
            System.out.println(f(n, p));
            nCasos -= 1;
        }
        input.close();
    }
}