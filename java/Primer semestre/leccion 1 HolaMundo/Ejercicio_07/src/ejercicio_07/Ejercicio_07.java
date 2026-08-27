
package ejercicio_07;
import java.util.Scanner;
public class Ejercicio_07 {

  
    public static void main(String[] args) {
        // Una compañia de venta de carros usados, paga a su personal de ventas
        //SALARIO DE $1000 mensuales mas una comision de $150 por cada carro v
        //vendido, mas el 5% del valor de la venta por carro.Cada mes el 
        //capturista de la empresa ingresa en la computadora los datos pertinentes.
        //Hacer un programa que calcule e imprima el salario mensual de un vendedor
        //dado.El salario de 1000 lo vamos a manejar como un dato constante
        //para asignarlo debemos usar la palabra "final"

        Scanner entrada = new Scanner (System.in);
            final int salario = 1000;
            int comision = 150, venta;
            float salarioMensual, ventaCarro,porcVenta,totalPrecio;
            
            System.out.println("Digite la cantidad de carros vencidos: ");
            venta = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite el precio de un carro: ");
            ventaCarro = Float.parseFloat(entrada.nextLine());
            
            comision *= venta;
            totalPrecio = ventaCarro * venta;
            porcVenta = totalPrecio + 0.05F;
            salarioMensual = salario + comision + porcVenta;
            
        
        
    }
    
}
