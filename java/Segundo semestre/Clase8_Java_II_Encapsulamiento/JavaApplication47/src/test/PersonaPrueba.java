package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona ("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 con su nombre es: " + persona1.getNombre());
        
        
        //Modificamos a tráves de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre ="Juan Ignacio";//Ya no se utiliza
        //System.out.println("nombre es= " + persona1.nombre);
        System.out.println("persona1 con su nombre modificamos: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " +persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        //Tarea:Crae otro de tipo persona,asignar valores de manera inicial
        //Y imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona ("Alejandra", 550000, false);
        System.out.println("persona2 con su nombre es: " + persona2.getNombre());
        
        //Modificamos a tráves de los métodos
        persona2.setNombre("Celeste");
        System.out.println("persona2 con su nombre modificamos: " + persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: " +persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: " + persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1);
    }
}
