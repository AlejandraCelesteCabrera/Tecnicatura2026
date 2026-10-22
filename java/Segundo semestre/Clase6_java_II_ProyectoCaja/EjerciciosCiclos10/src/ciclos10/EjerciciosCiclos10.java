
package ciclos10;

import javax.swing.JOptionPane;

public class EjerciciosCiclos10 {
    public static void main(String[] args) {
        int numero, suma = 0;
        for(int i=1; i <= 10; i++){
            numero= Integer.parseInt(JOptionPane.showInputDialog("DIGITE UN NÚMERO: "));
            suma += numero;
        }
        System.out.println("\nLa suma de todos los números es: "+suma);
        JOptionPane.showConfirmDialog(null,"\nLa suma de todos los números es: " + suma);
    }
    
}
