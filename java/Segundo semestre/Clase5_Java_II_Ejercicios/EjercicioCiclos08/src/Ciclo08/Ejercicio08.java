/*
Ejercicio8: Pedir un número N y mostar todos los números de 1 al N.
 */
package Ciclo08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args) {
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        int i = 1;
        while (i <= numero){
            System.out.println(i);
            JOptionPane.showConfirmDialog(null,i);
            i++;
        }
    }
}
