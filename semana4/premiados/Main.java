import java.util.Scanner;

public class Main {

    public static int MMC(int a, int b, int x, int y) {
        if (a*x == b*y) {
            return a*x;
        } else {
            if (a*x < b*y) {
                return MMC(a,b,x+1,y);
            }
            return MMC(a,b,x,y+1);
        }
    }

    public static int quantidadePremios(int n, int a, int b, int c, int x, int y) {
        int abMMC = MMC(a,b,x,y);
        int bcMMC = MMC(b,c,x,y);
        int acMMC = MMC(a,c,x,y);
        int abcMMC = MMC(abMMC,c,x,y);
        return n/a + n/b + n/c - n/abMMC - n/bcMMC - n/acMMC + n/abcMMC;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();
        while (nCasos > 0) {
            int n = input.nextInt();
            int a = input.nextInt();
            int b = input.nextInt();
            int c = input.nextInt();
            int x = 1;
            int y = 1;
            int resultado = quantidadePremios(n,a,b,c,x,y);
            System.out.println(resultado);
            nCasos--;
        }
    }
}
