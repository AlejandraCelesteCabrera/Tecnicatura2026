
package ejercicio6;

import java.util.Scanner;
public class Ejercicio6 {
 //Guillermo tien N dolares.Luis tiene la mitad de lo que posee Guillermo
     // Juan tiene la miatd de lo que popsee Luis y guillermo juntos.
     // Hacer un programa que calcule e imprima la cantidad de dinero 
     //que tiene entre los tres.
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        float guillermo,luis,juan,total;
        System.out.println("Digite la cantidad de dinero de Guillermo");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan =(luis + guillermo)/2;
        total = luis+guillermo+luis;
        System.out.println("El dinero de Luis es: U$"+luis);
        System.out.println("El dinero de Juan es: U$"+juan);
        System.out.println("El total de dinero entre los 3 es: U$"+total);
       
        
    }
    
    
}
