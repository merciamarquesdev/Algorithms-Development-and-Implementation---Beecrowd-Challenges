import java.util.Scanner;

public class Main {
    
    public static long T(long n,long p){
        if(p == 1 || p == n){
            return 1;
        }
        else{
            return ((T(n-1,p)*p) + T(n-1,p-1));
        }
    }
    
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();
        
        while (nCasos > 0){
            int n = input.nextInt();
            int p = input.nextInt();
            long resultado = T(n,p);
            System.out.println(resultado);
            nCasos--;
        }
    }
}
