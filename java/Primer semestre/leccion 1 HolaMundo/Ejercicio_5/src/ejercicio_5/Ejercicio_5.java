
package ejercicio_5;

import java.util.Scanner;
public class Ejercicio_5 {

    
    public static void main(String[] args) {
        
         Scanner entrada = new Scanner (System.in);
            System.out.println("Digite la nota1");
            int nota1 = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite la nota2");
            int nota2 = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite nota3");
            int nota3 = Integer.parseInt(entrada.nextLine());
            
            var promedio = (nota1 + nota2 + nota3)/ 3;
            System.out.println("promedio = " + promedio);
    }
    
}
