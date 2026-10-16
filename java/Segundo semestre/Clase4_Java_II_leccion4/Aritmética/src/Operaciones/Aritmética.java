
package Operaciones;


public class Aritmética {
   //Atributos de la clase
    int a;
    int b;
       
    //El constructor es un método especial
    public Aritmética(){ // Constructor 1 vacio
        System.out.println("Se esta ejecutando este constructor número uno");
    }
    //Estamos viendo lo que se llama sobre carga de constructores
    public Aritmética(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor número dos");
    }
    
    //Métodos
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = "+resultado);
    }
    
    public int sumarConRetorno(){
       // int resultado = a + b;
       return this.a + this.b;     
    }
    
    public int sumarConArgumentos(int arg1, int arg2){ // no se puede poner var en lugar de int
         this.a  = arg1; //El argumento a se asigna al atributo this.a
         this.b = arg2; 
        // return a + b;
        return sumarConRetorno();
    }
}