/*
Ejercicio 3: Leer números hasta que se introduzca un cero 
Para cada indicar si es par o impar
Primero lo haremos con clase Scanner
Lueho con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;

 class Ejercicio03 {
     public static void main(String[] args) {
         int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0){
            if (numero % 2 == 0){
               JOptionPane.showMessageDialog(null,"El número ingresado " +numero+"es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null,"El número " +numero+" es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado es "+numero+" finaliza el programa");
    
     }
    
}
