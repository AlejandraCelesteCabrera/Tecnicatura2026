
package Operaciones;


public class PruebaAritmética {
    public static void main(String[] args) {
        int a = 10; // Variable locales
        int b =7; // Memoria stack "almecena la memoria del objeto"
        miMetodo(); //Llamamos al método nuevo
        Aritmética aritmetica1 = new Aritmética();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1 = null; //(para que quede limpio para que no quede ningun residuo)
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
       
    }  
    
    public static void miMetodo (){
        //Int a = 10;
        System.out.println("Aquí hay otro método");
    }
}
