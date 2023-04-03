package org.example;

import java.util.Scanner;

public class Main {
    public static int metodo1(int a, int b) {
        int resultado;

        if (a >= b) {
            resultado = b / 2;
        }
        else {
            resultado = a / 2;
        }
        return resultado;
    }

    public static int metodo2(int a, int b) {
        int resultado = 0;
        if (a >= b) {
            while (b > 0) {
                if (b * 4 <= a) {
                    resultado = b;
                    break;
                }
                else {
                    b -= 1;
                }
            }
        }

        else {
            while (a > 0) {
                if (a * 4 <= b) {
                    resultado = a;
                    break;
                }
                else {
                    a -= 1;
                }
            }
        }

        return resultado;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nCasos = input.nextInt();

        while (nCasos > 0) {
            int a = input.nextInt();
            int b = input.nextInt();

            int m1 = metodo1(a, b);
            int m2 = metodo2(a, b);

            if (m1 >= m2) {
                System.out.println(m1);
            }
            else {
                System.out.println(m2);
            }

            nCasos -= 1;
        }
        input.close();
    }
}