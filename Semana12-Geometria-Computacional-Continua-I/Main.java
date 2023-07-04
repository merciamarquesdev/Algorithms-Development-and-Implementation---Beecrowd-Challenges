import java.util.Scanner;
import java.lang.Math; 

public class Main {
    public static double areaVermelha(int a, int b, int c) {
        double s = (a+b+c)/2.0;
        double aux = (s*(s-a)*(s-b)*(s-c));
        double r = aux/(Math.pow(s,2));
        double areaVermelha = Math.PI*r;
    
        return areaVermelha;
    }

    public static double areaVioleta(int a, int b, int c,double areaVermelha) {
        double s = (a+b+c)/2.0;
        double aux = (s*(s-a)*(s-b)*(s-c));
        double areaTriang = Math.sqrt(aux);
        double areaVioleta = areaTriang - areaVermelha;
    
        return areaVioleta;
    }

    public static double areaAmarela(int a, int b, int c) {
        double s = (a+b+c)/2.0;
        double aux = (s*(s-a)*(s-b)*(s-c));
        double areaTriang = Math.sqrt(aux);
        double R = Math.pow((a*b*c),2)/(aux*Math.pow(4,2));
        
        double areaAmarela = (Math.PI*R) - areaTriang;

        return areaAmarela;
    }

    public static void fazendoJardins() {
        Scanner scanner = new Scanner(System.in);
        int nCasos = scanner.nextInt();
        while (nCasos > 0) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();

            double vermelha = areaVermelha(a, b, c);
            double violeta = areaVioleta(a, b, c, vermelha);
            double amarela = areaAmarela(a, b, c);
            
            System.out.printf("%.2f %.2f %.2f",amarela,violeta,vermelha); 
            nCasos -= 1;
        }
        scanner.close();
    }

    public static void main(String[] args) {
        fazendoJardins();
    }
}
