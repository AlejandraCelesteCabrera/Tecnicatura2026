
package javaapplication24;

//Ejercicio 2: Hacer un programa que calcule el cuadro de una suma,
//el usuario debe ingresar el valor de a y el valor de b.
//Formula: (a+b)2=a2+b2+2*a*b
//Para esto deberán utilizar la clase Math y un método llamado pow
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        double a,b,resultado;
        System.out.println("Ingrese el nuúmero de a: ");
        a = entrada.nextDouble();
        System.out.println("Ingrese el número de b: ");
        b = entrada.nextDouble();
        
        resultado = Math.pow(a, 2) + Math.pow(b,2) + (2*a*b);
        System.out.println("resultado = " + resultado);
        
    }
}
