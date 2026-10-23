
package Operaciones;


public class PruebaAritmética {
    public static void main(String[] args) {
        int a = 10; // Variable locales
        int b = 7 ; // Memoria stack "almecena la memoria del objeto"
        miMetodo(); //Llamamos al método nuevo
        Aritmética aritmetica1 = new Aritmética();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
      // aritmetica1 = null; //(para que quede limpio para que no quede ningun residuo)
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memora heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " +resultado);
        
        System.out.println("aritmetica|: "+aritmetica1.a);
        System.out.println("aritmetica1: "+aritmetica1.b);
        
        Aritmética aritmetica2 = new Aritmética(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null;
        //system.gc(); //recolector de basura, pero es innecesario    
        Persona persona = new Persona("Ariel","Betancud"); 
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido "+persona.apellido);
    }  
    
    //Modularidad creamos un nuevo método
    public static void miMetodo (){
        //Int a = 10;
        System.out.println("Aquí hay otro método");
    }
}
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
        super(); //Llamada al constructor de la clase Pader object
       // Imprimir imprimir = new Imprimir();
       new Imprimir().imprimir(this);
        this.nombre = nombre ;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
    
}

class Imprimir{
    public Imprimir(){
        super(); // el constructor desde la clase imprimir
        
    }
    public void imprimir(Persona persona){
        System.out.println("persona desde la clase imprimir: " + persona);
        System.out.println("Impresión del objeto actual (this): "+this);
        
    }
}