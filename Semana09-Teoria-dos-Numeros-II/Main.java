import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        numeroComposto();
    }

    public static void geraCrivo(int n, ArrayList<Integer> C) {
        C.add(0);
        for (int i = 1; i <= n; i++) {
            C.add(i);
        }
        int t = 2;
        for (int i = 1; i <= n / 2; i++) {
            C.set(t, 2);
            t += 2;
        }
        for (int i = 3; i <= Math.sqrt(n); i++) {
            if (C.get(i) == i) {
                t = i * i;
                int d = i + i;
                while (t <= n) {
                    if (C.get(t) == t) {
                        C.set(t, i);
                    }
                    t += d;
                }
            }
        }
    }

    public static void geraPrimos(long n, ArrayList<Integer> crivo, ArrayList<Integer> P) {
        for (int i = 2; i <= n; i++) {
            if (crivo.get(i) == i) {
                P.add(i);
            }
        }
    }

    public static boolean ehPrimo(long n, ArrayList<Integer> tabelaPrimos) {
        for (int i = 0; i < tabelaPrimos.size(); i++) {
            if (n % tabelaPrimos.get(i) == 0) {
                if (n != tabelaPrimos.get(i)) {
                    return false;
                } else {
                    return true;
                }
            }
        }
        return true;
    }

    public static String ehComposto(boolean primo) {
        if (primo) {
            return "N";
        } else {
            return "S";
        }
    }

    public static void numeroComposto() {
        int size = (int) Math.pow(10,7);
        ArrayList<Integer> C = new ArrayList<Integer>(size);
        ArrayList<Integer> P = new ArrayList<Integer>(size/10);
        geraCrivo(size, C);
        geraPrimos(size, C, P);
        int np = P.size();
        Scanner scanner = new Scanner(System.in);
        int nCasos = scanner.nextInt();
        while (nCasos > 0) {
            long n = scanner.nextLong();
            boolean primo = ehPrimo(n, P);
            String resultado = ehComposto(primo);
            System.out.println(resultado);
            nCasos--;
        }
    }
}
