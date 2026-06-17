
package javaapplication24;

import java.util.Scanner;

public class JavaApplication24 {

   public static void main(String[] args) {
      //Ejercicio 1: Construir un programa que, dado un número total de
//horas, devuelve el número de semanas, días y horas equivalentes.
//Por ejemplo dado un total de 1000 horas debe mostrar 5 semanas,
//6 días y 16 horas

  
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el total de horas: ");
        int horasTotales = entrada.nextInt();
        int semanas = horasTotales / 168;
        int resto = horasTotales % 168;
        
        int dias = resto /24;
        int horas = resto % 24;
        
        System.out.println("La semana equivale a: ");
        System.out.println(semanas + "semanas, " );
        System.out.println(dias +"dias");
        System.out.println(horas+"horas");
    }
    
}

